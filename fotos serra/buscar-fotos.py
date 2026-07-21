#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Busca na biblioteca de imagens da LeAnge Serra (catalogo-imagens.csv).

Uso (rodar de dentro de "fotos serra/", ou passar --csv):
    python buscar-fotos.py cachorro piscina serra
    python buscar-fotos.py "cafe da manha" --cat Gastronomia --limit 15
    python buscar-fotos.py suite lareira --fonte foto-real
    python buscar-fotos.py banheira --json          # saida JSON p/ agente
    python buscar-fotos.py                            # sem termos: mostra estatisticas

Ranking: cobre quantos termos batem (peso maior p/ nome/keywords/categoria),
busca sem acento e sem diferenciar maiuscula/minuscula.
Retorna o CAMINHO do arquivo pronto pra usar:
  - foto-real  -> _renomeadas/<arquivo>
  - raw-preview-> _raw-renomeados/<preview>  (master original: <nome_original> na pasta base)
"""
import os, sys, csv, json, argparse, unicodedata
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CSV = os.path.join(BASE, "catalogo-imagens.csv")

def fold(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return s

# campo -> peso na pontuacao
WEIGHTS = {
    "novo_nome": 3, "palavras_chave": 3, "categoria": 2, "ambiente": 2,
    "objetos": 2, "descricao": 1, "usos": 1, "estilo": 1,
    "iluminacao": 1, "pessoas": 1, "observacoes": 1, "nome_original": 1,
}

def load(csv_path):
    with open(csv_path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))

def score(row, terms):
    cobertura = 0
    peso = 0
    for t in terms:
        achou = False
        for campo, w in WEIGHTS.items():
            if t in fold(row.get(campo, "")):
                peso += w
                achou = True
        if achou:
            cobertura += 1
    return cobertura, peso

def caminho(row):
    if row["fonte"] == "foto-real":
        return os.path.join(BASE, "_renomeadas", row["novo_nome"])
    return os.path.join(BASE, "_raw-renomeados", row["novo_nome"])

def main():
    ap = argparse.ArgumentParser(add_help=True, description="Busca de fotos da LeAnge Serra")
    ap.add_argument("termos", nargs="*", help="palavras-chave (sem acento tudo bem)")
    ap.add_argument("--csv", default=DEFAULT_CSV)
    ap.add_argument("--cat", default=None, help="filtra por categoria (substring)")
    ap.add_argument("--fonte", default=None, choices=["foto-real", "raw-preview"])
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = load(args.csv)

    if args.cat:
        cf = fold(args.cat)
        rows = [r for r in rows if cf in fold(r["categoria"])]
    if args.fonte:
        rows = [r for r in rows if r["fonte"] == args.fonte]

    # sem termos: estatisticas
    if not args.termos:
        from collections import Counter
        c = Counter(r["categoria"] for r in rows)
        fo = Counter(r["fonte"] for r in rows)
        print(f"Biblioteca: {len(rows)} imagens  |  {dict(fo)}")
        print("Por categoria:")
        for k, v in c.most_common():
            print(f"  {v:4d}  {k}")
        print('\nExemplo: python buscar-fotos.py cachorro piscina serra')
        return

    terms = [fold(t) for t in args.termos if t.strip()]
    scored = []
    for r in rows:
        cob, pes = score(r, terms)
        if cob > 0:
            scored.append((cob, pes, r))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    top = scored[:args.limit]

    if args.json:
        out = [{
            "score": f"{cob}/{len(terms)} termos, peso {pes}",
            "cobertura": cob, "peso": pes,
            "novo_nome": r["novo_nome"], "categoria": r["categoria"],
            "fonte": r["fonte"], "caminho": caminho(r),
            "master_original": (os.path.join(BASE, r["nome_original"]) if r["fonte"] == "raw-preview" else caminho(r)),
            "descricao": r["descricao"],
        } for cob, pes, r in top]
        print(json.dumps({"query": args.termos, "total_encontrado": len(scored), "resultados": out}, ensure_ascii=False, indent=2))
        return

    print(f'Busca: {" ".join(args.termos)}  ->  {len(scored)} encontradas (mostrando {len(top)})\n')
    for i, (cob, pes, r) in enumerate(top, 1):
        print(f"{i:2d}. [{cob}/{len(terms)} termos] {r['categoria']}  ({r['fonte']})")
        print(f"    {caminho(r)}")
        if r["fonte"] == "raw-preview":
            print(f"    master: {os.path.join(BASE, r['nome_original'])}")
        d = r["descricao"]
        print(f"    {d[:160]}{'...' if len(d) > 160 else ''}")
        print()

if __name__ == "__main__":
    main()
