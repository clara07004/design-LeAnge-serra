/**
 * validar-overflow.js — Detecta conteúdo (texto) cortado/transbordando dentro do canvas.
 *
 * A validar-dimensao.py garante que o PNG tem 1080x1350. Este validador é complementar:
 * renderiza o HTML no mesmo viewport e checa se ALGUM elemento com texto ultrapassa as
 * bordas do canvas (right>W, bottom>H, left<0, top<0) ou é clipado por um ancestral com
 * overflow:hidden. Pega o caso clássico de info bar / rodapé cortado no canto que a
 * validação de dimensão NÃO detecta (o canvas continua 1080x1350, mas o texto sangra).
 *
 * Uso:
 *   node validar-overflow.js <pasta-ou-html> [<html> ...] [--w 1080] [--h 1350]
 *   node validar-overflow.js "conteudo/carrosseis/PERIODO/DIA/instagram"
 *
 * Exit 0 = tudo dentro do canvas. Exit 1 = há conteúdo cortado (NÃO publicar).
 * Exit 2 = erro de execução (Playwright ausente, nenhum HTML, etc).
 */
const path = require("path");
const fs = require("fs");
const { execSync } = require("child_process");

// ── Localizar o módulo playwright (robusto a mudança de hash do cache npx) ─────
function resolvePlaywright() {
  const tryRequire = (p) => { try { return require(p); } catch (_) { return null; } };
  let pw = tryRequire("playwright") || tryRequire("playwright-core");
  if (pw) return pw;

  const candidates = [];
  try {
    const groot = execSync("npm root -g", { encoding: "utf8" }).trim();
    candidates.push(path.join(groot, "playwright"), path.join(groot, "playwright-core"));
  } catch (_) {}
  const local = process.env.LOCALAPPDATA || process.env.APPDATA;
  if (local) {
    const npxDir = path.join(local, "npm-cache", "_npx");
    try {
      for (const d of fs.readdirSync(npxDir)) {
        candidates.push(
          path.join(npxDir, d, "node_modules", "playwright"),
          path.join(npxDir, d, "node_modules", "playwright-core"),
        );
      }
    } catch (_) {}
  }
  for (const c of candidates) {
    pw = tryRequire(c);
    if (pw) return pw;
  }
  throw new Error(
    "Playwright nao encontrado. Rode `npx.cmd playwright install chromium` na raiz do projeto.",
  );
}

// ── Argumentos ────────────────────────────────────────────────────────────────
let W = 1080, H = 1350;
const targets = [];
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === "--w") { W = parseInt(argv[++i], 10); continue; }
  if (argv[i] === "--h") { H = parseInt(argv[++i], 10); continue; }
  targets.push(argv[i]);
}

function collectHtml(t) {
  const stat = fs.statSync(t);
  if (stat.isDirectory()) {
    return fs
      .readdirSync(t)
      .filter((f) => /^slide-.*\.html$/i.test(f) || /^post-.*\.html$/i.test(f))
      .sort()
      .map((f) => path.join(t, f));
  }
  return [t];
}

(async () => {
  if (!targets.length) {
    console.error("Uso: node validar-overflow.js <pasta-ou-html> [--w 1080] [--h 1350]");
    process.exit(2);
  }
  const files = targets.flatMap(collectHtml);
  if (!files.length) {
    console.error("Nenhum HTML (slide-*.html / post-*.html) encontrado.");
    process.exit(2);
  }

  const { chromium } = resolvePlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: W, height: H },
    deviceScaleFactor: 1,
  });

  let anyFail = false;
  const TOL = 3; // px de tolerância p/ arredondamento e letter-spacing residual

  for (const file of files) {
    const url = "file:///" + path.resolve(file).replace(/\\/g, "/");
    try {
      await page.goto(url, { waitUntil: "networkidle", timeout: 30000 });
    } catch (_) {
      await page.goto(url, { waitUntil: "load", timeout: 30000 });
    }
    try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch (_) {}

    const issues = await page.evaluate(({ W, H, TOL }) => {
      const out = [];
      const seen = new Set();
      for (const el of document.querySelectorAll("*")) {
        let hasText = false;
        for (const n of el.childNodes) {
          if (n.nodeType === 3 && n.textContent.trim().length > 0) { hasText = true; break; }
        }
        if (!hasText) continue;
        const s = getComputedStyle(el);
        if (s.visibility === "hidden" || s.display === "none" || parseFloat(s.opacity) === 0) continue;
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) continue;
        const label = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 42);

        const push = (type, px) => {
          const key = type + "|" + label;
          if (seen.has(key)) return;
          seen.add(key);
          out.push({ type, px: Math.round(px), tag: el.tagName, text: label });
        };
        if (r.right > W + TOL) push("transborda-direita", r.right - W);
        else if (r.left < -TOL) push("transborda-esquerda", -r.left);
        if (r.bottom > H + TOL) push("transborda-base", r.bottom - H);
        else if (r.top < -TOL) push("transborda-topo", -r.top);

        // Texto clipado dentro da própria caixa com overflow:hidden
        const ovf = s.overflow + s.overflowX + s.overflowY;
        if (/hidden|clip/.test(ovf)) {
          const dx = el.scrollWidth - el.clientWidth;
          const dy = el.scrollHeight - el.clientHeight;
          if (dx > TOL || dy > TOL) push("texto-clipado", Math.max(dx, dy));
        }
      }
      return out;
    }, { W, H, TOL });

    if (issues.length) {
      anyFail = true;
      console.log(`FALHA  ${path.basename(file)} — ${issues.length} elemento(s) fora do canvas ${W}x${H}:`);
      for (const it of issues.slice(0, 15)) {
        console.log(`   - ${it.type} +${it.px}px  <${it.tag}> "${it.text}"`);
      }
    } else {
      console.log(`OK     ${path.basename(file)} — nada cortado`);
    }
  }

  await browser.close();
  if (anyFail) {
    console.log("\nConteudo cortado detectado. NAO publicar — corrigir o HTML e re-renderizar.");
    process.exit(1);
  }
  console.log(`\nTodos os ${files.length} slide(s) OK — nenhum texto ultrapassa ${W}x${H}.`);
})().catch((e) => {
  console.error("ERRO validador:", e.message);
  process.exit(2);
});
