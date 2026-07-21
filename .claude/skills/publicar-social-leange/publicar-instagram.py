"""
publicar-instagram.py — Publicação automática no Instagram via Meta Graph API

Uso:
  # Publicação imediata (terça a sexta)
  python publicar-instagram.py --tipo imagem --imagem caminho/para/post.png --legenda "texto"
  python publicar-instagram.py --tipo carrossel --pasta caminho/para/instagram/ --legenda "texto"

  # Publicação agendada (sábado e domingo — obrigatório)
  python publicar-instagram.py --tipo carrossel --pasta caminho/ --legenda "texto" --agendar "05/07/2026 10:00"
  python publicar-instagram.py --tipo imagem --imagem post.png --legenda "texto" --agendar "06/07/2026 09:30"

  # Ver agendamentos pendentes na conta
  python publicar-instagram.py --listar-agendados

Formato de data/hora: DD/MM/AAAA HH:MM (fuso horário local do sistema)

Credenciais esperadas em credentials/ (raiz do projeto):
  meta_access_token.txt  — token de acesso Meta (long-lived, válido 60 dias)
  meta_ig_user_id.txt    — ID do usuário Instagram Business/Creator
  imgbb_api_key.txt      — chave da API imgbb para hospedar imagens publicamente

Dependências: httpx (já incluído no pip install openai)
  pip install openai
"""

import argparse
import base64
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

# ── Caminhos ─────────────────────────────────────────────────────────────────
# Este script fica em .claude/skills/publicar-social-leange/ — 4 níveis abaixo da raiz
REPO_ROOT = Path(__file__).parent.parent.parent.parent
CREDENTIALS_DIR = REPO_ROOT / "credentials"

# ── Configuração da API ───────────────────────────────────────────────────────
# Atualizar GRAPH_API_VERSION quando a Meta descontinuar a versão atual.
# Versões suportadas: https://developers.facebook.com/docs/graph-api/changelog
GRAPH_API_VERSION = "v22.0"
GRAPH_API = f"https://graph.facebook.com/{GRAPH_API_VERSION}"
IMGBB_API = "https://api.imgbb.com/1/upload"


# ── Leitura de credenciais ───────────────────────────────────────────────────
def ler_credencial(nome_arquivo: str) -> str:
    caminho = CREDENTIALS_DIR / nome_arquivo
    if not caminho.exists():
        print(f"ERRO: credencial não encontrada: credentials/{nome_arquivo}", file=sys.stderr)
        print(f"  Crie o arquivo com o valor correspondente em credentials/.", file=sys.stderr)
        sys.exit(2)
    valor = caminho.read_text(encoding="utf-8").strip()
    if not valor or valor.startswith("PREENCHER"):
        print(f"ERRO: credentials/{nome_arquivo} não foi preenchido.", file=sys.stderr)
        sys.exit(2)
    return valor


# ── Upload de imagem para imgbb ──────────────────────────────────────────────
def upload_imgbb(caminho_imagem: str, imgbb_key: str) -> str:
    """Faz upload de uma imagem local para imgbb e retorna a URL pública."""
    with open(caminho_imagem, "rb") as f:
        imagem_b64 = base64.b64encode(f.read()).decode("utf-8")

    resposta = httpx.post(
        IMGBB_API,
        data={"key": imgbb_key, "image": imagem_b64},
        timeout=60,
    )

    if resposta.status_code != 200:
        print(f"ERRO imgbb: {resposta.status_code} — {resposta.text}", file=sys.stderr)
        sys.exit(3)

    dados = resposta.json()
    if not dados.get("success"):
        print(f"ERRO imgbb: {dados}", file=sys.stderr)
        sys.exit(3)

    url = dados["data"]["url"]
    print(f"  imgbb: {Path(caminho_imagem).name} -> {url}")
    return url


# ── Converter data/hora para timestamp Unix UTC ──────────────────────────────
def parse_agendamento(data_hora_str: str) -> int:
    """Converte 'DD/MM/AAAA HH:MM' (horário local) para timestamp Unix UTC."""
    try:
        dt_local = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
    except ValueError:
        print(f"ERRO: formato de data inválido '{data_hora_str}'. Use DD/MM/AAAA HH:MM", file=sys.stderr)
        sys.exit(1)

    dt_utc = dt_local.astimezone(timezone.utc)
    ts = int(dt_utc.timestamp())

    agora = int(datetime.now(timezone.utc).timestamp())
    if ts < agora + 20 * 60:
        print("ERRO: agendamento muito próximo. Mínimo: 20 minutos no futuro.", file=sys.stderr)
        sys.exit(1)
    if ts > agora + 75 * 24 * 60 * 60:
        print("ERRO: agendamento muito distante. Máximo: 75 dias no futuro.", file=sys.stderr)
        sys.exit(1)

    return ts


# ── Criar container de mídia (imagem única) ──────────────────────────────────
def criar_container_imagem(ig_user_id: str, token: str, image_url: str,
                           caption: str = "", scheduled_ts: int = None) -> str:
    payload = {"image_url": image_url, "caption": caption, "access_token": token}
    if scheduled_ts:
        payload["published"] = "false"
        payload["scheduled_publish_time"] = str(scheduled_ts)

    resposta = httpx.post(f"{GRAPH_API}/{ig_user_id}/media", data=payload, timeout=30)
    dados = resposta.json()
    if "error" in dados:
        print(f"ERRO criar container: {dados['error']['message']}", file=sys.stderr)
        sys.exit(4)
    return dados["id"]


# ── Criar container filho (para carrossel) ───────────────────────────────────
def criar_container_filho(ig_user_id: str, token: str, image_url: str) -> str:
    resposta = httpx.post(
        f"{GRAPH_API}/{ig_user_id}/media",
        data={"image_url": image_url, "is_carousel_item": "true", "access_token": token},
        timeout=30,
    )
    dados = resposta.json()
    if "error" in dados:
        print(f"ERRO criar filho: {dados['error']['message']}", file=sys.stderr)
        sys.exit(4)
    return dados["id"]


# ── Criar container de carrossel ─────────────────────────────────────────────
def criar_container_carrossel(ig_user_id: str, token: str, children_ids: list,
                               caption: str = "", scheduled_ts: int = None) -> str:
    payload = {
        "media_type": "CAROUSEL",
        "children": ",".join(children_ids),
        "caption": caption,
        "access_token": token,
    }
    if scheduled_ts:
        payload["published"] = "false"
        payload["scheduled_publish_time"] = str(scheduled_ts)

    resposta = httpx.post(f"{GRAPH_API}/{ig_user_id}/media", data=payload, timeout=30)
    dados = resposta.json()
    if "error" in dados:
        print(f"ERRO criar carrossel: {dados['error']['message']}", file=sys.stderr)
        sys.exit(4)
    return dados["id"]


# ── Aguardar container ficar pronto ──────────────────────────────────────────
def aguardar_container(ig_user_id: str, token: str, creation_id: str, max_tentativas: int = 10):
    """Verifica o status do container. Aborta se não ficar FINISHED no prazo."""
    for i in range(max_tentativas):
        resposta = httpx.get(
            f"{GRAPH_API}/{creation_id}",
            params={"fields": "status_code", "access_token": token},
            timeout=15,
        )
        dados = resposta.json()
        status = dados.get("status_code", "")
        if status == "FINISHED":
            return
        if status == "ERROR":
            print(f"ERRO: container retornou ERROR — {dados}", file=sys.stderr)
            print("  Publicação abortada. Nada foi publicado.", file=sys.stderr)
            sys.exit(4)
        print(f"  aguardando container... ({status}) — tentativa {i+1}/{max_tentativas}")
        time.sleep(5)

    # Timeout — abortar, não publicar em estado incerto
    print("ERRO: timeout aguardando container — publicação abortada.", file=sys.stderr)
    print("  Nada foi publicado. Tente novamente em alguns minutos.", file=sys.stderr)
    sys.exit(4)


# ── Publicar container ───────────────────────────────────────────────────────
def publicar_container(ig_user_id: str, token: str, creation_id: str) -> str:
    resposta = httpx.post(
        f"{GRAPH_API}/{ig_user_id}/media_publish",
        data={"creation_id": creation_id, "access_token": token},
        timeout=30,
    )
    dados = resposta.json()
    if "error" in dados:
        print(f"ERRO publicar: {dados['error']['message']}", file=sys.stderr)
        sys.exit(4)
    return dados["id"]


# ── Validar legenda ───────────────────────────────────────────────────────────
def validar_legenda(legenda: str):
    """Valida tamanho e número de hashtags antes de enviar à API."""
    if len(legenda) > 2200:
        print(f"ERRO: legenda com {len(legenda)} caracteres — máximo permitido é 2.200.", file=sys.stderr)
        print("  Encurte a legenda antes de publicar.", file=sys.stderr)
        sys.exit(1)

    hashtags = [p for p in legenda.split() if p.startswith("#")]
    if len(hashtags) > 30:
        print(f"ERRO: legenda com {len(hashtags)} hashtags — máximo permitido é 30.", file=sys.stderr)
        sys.exit(1)


# ── Listar posts agendados ────────────────────────────────────────────────────
def listar_agendados(ig_user_id: str, token: str):
    resposta = httpx.get(
        f"{GRAPH_API}/{ig_user_id}/media",
        params={"fields": "id,media_type,timestamp,scheduled_publish_time,caption", "access_token": token},
        timeout=15,
    )
    dados = resposta.json()
    if "error" in dados:
        print(f"ERRO: {dados['error']['message']}", file=sys.stderr)
        sys.exit(4)

    items = [i for i in dados.get("data", []) if i.get("scheduled_publish_time")]
    if not items:
        print("Nenhum post agendado encontrado.")
        return

    print(f"\nPosts agendados ({len(items)}):")
    for item in items:
        tipo = item.get("media_type", "?")
        agendado = item.get("scheduled_publish_time", "?")
        preview = (item.get("caption", "") or "")[:60]
        print(f"  ID: {item['id']} | {tipo} | Agendado: {agendado}")
        print(f"  Legenda: {preview}...")
        print()


# ── Fluxo: imagem única ──────────────────────────────────────────────────────
def publicar_imagem(caminho: str, legenda: str, ig_user_id: str, token: str,
                    imgbb_key: str, scheduled_ts: int = None):
    validar_legenda(legenda)
    sufixo = f" (agendado)" if scheduled_ts else ""
    print(f"\nPublicando imagem{sufixo}: {caminho}")

    print("1/3  fazendo upload para imgbb...")
    url = upload_imgbb(caminho, imgbb_key)

    print("2/3  criando container de mídia...")
    creation_id = criar_container_imagem(ig_user_id, token, url, legenda, scheduled_ts)
    aguardar_container(ig_user_id, token, creation_id)

    if scheduled_ts:
        dt = datetime.fromtimestamp(scheduled_ts).strftime("%d/%m/%Y %H:%M")
        print(f"\nOK — post agendado para {dt}. Creation ID: {creation_id}")
        print("     Use --listar-agendados para confirmar.")
    else:
        print("3/3  publicando no Instagram...")
        media_id = publicar_container(ig_user_id, token, creation_id)
        print(f"\nOK — post publicado. Media ID: {media_id}")
        print(f"     URL: https://www.instagram.com/p/{media_id}/")
    return creation_id


# ── Fluxo: carrossel ─────────────────────────────────────────────────────────
def publicar_carrossel(pasta: str, legenda: str, ig_user_id: str, token: str,
                       imgbb_key: str, scheduled_ts: int = None):
    validar_legenda(legenda)
    slides = sorted([str(p) for p in Path(pasta).glob("slide-*.png")])

    if not slides:
        print(f"ERRO: nenhum slide-XX.png encontrado em {pasta}", file=sys.stderr)
        sys.exit(1)
    if len(slides) > 10:
        print("AVISO: Instagram aceita no máximo 10 slides. Usando os primeiros 10.")
        slides = slides[:10]

    sufixo = " (agendado)" if scheduled_ts else ""
    print(f"\nPublicando carrossel{sufixo}: {len(slides)} slides em {pasta}")

    print(f"1/{len(slides)+2}  fazendo upload dos slides para imgbb...")
    urls = []
    for i, slide in enumerate(slides):
        print(f"  [{i+1}/{len(slides)}] {Path(slide).name}")
        url = upload_imgbb(slide, imgbb_key)
        urls.append(url)

    print(f"{len(slides)+1}/{len(slides)+2}  criando containers filhos...")
    children_ids = []
    for i, url in enumerate(urls):
        print(f"  [{i+1}/{len(urls)}] criando item...")
        filho_id = criar_container_filho(ig_user_id, token, url)
        children_ids.append(filho_id)
        time.sleep(1)

    print(f"{len(slides)+1}/{len(slides)+2}  criando container carrossel...")
    creation_id = criar_container_carrossel(ig_user_id, token, children_ids, legenda, scheduled_ts)
    aguardar_container(ig_user_id, token, creation_id)

    if scheduled_ts:
        dt = datetime.fromtimestamp(scheduled_ts).strftime("%d/%m/%Y %H:%M")
        print(f"\nOK — carrossel agendado para {dt}. Creation ID: {creation_id}")
        print("     Use --listar-agendados para confirmar.")
    else:
        print(f"{len(slides)+2}/{len(slides)+2}  publicando no Instagram...")
        media_id = publicar_container(ig_user_id, token, creation_id)
        print(f"\nOK — carrossel publicado. Media ID: {media_id}")
        print(f"     URL: https://www.instagram.com/p/{media_id}/")
    return creation_id


# ── Entry point ──────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Publica no Instagram via Meta Graph API")
    parser.add_argument("--tipo", choices=["imagem", "carrossel"])
    parser.add_argument("--imagem", help="Caminho do PNG (para --tipo imagem)")
    parser.add_argument("--pasta", help="Pasta com slide-XX.png (para --tipo carrossel)")
    parser.add_argument("--legenda", help="Texto da legenda do post")
    parser.add_argument("--agendar", metavar="DD/MM/AAAA HH:MM",
                        help="Agendar publicação. Obrigatório para sábado e domingo.")
    parser.add_argument("--listar-agendados", action="store_true",
                        help="Listar posts agendados na conta.")
    args = parser.parse_args()

    token = ler_credencial("meta_access_token.txt")
    ig_user_id = ler_credencial("meta_ig_user_id.txt")

    if args.listar_agendados:
        listar_agendados(ig_user_id, token)
        return

    if not args.tipo:
        print("ERRO: --tipo é obrigatório (imagem ou carrossel)", file=sys.stderr)
        sys.exit(1)
    if not args.legenda:
        print("ERRO: --legenda é obrigatório", file=sys.stderr)
        sys.exit(1)

    imgbb_key = ler_credencial("imgbb_api_key.txt")
    scheduled_ts = parse_agendamento(args.agendar) if args.agendar else None

    if scheduled_ts:
        dt = datetime.fromtimestamp(scheduled_ts).strftime("%d/%m/%Y %H:%M")
        print(f"  Agendamento: {dt} (local)")

    if args.tipo == "imagem":
        if not args.imagem:
            print("ERRO: --imagem é obrigatório para --tipo imagem", file=sys.stderr)
            sys.exit(1)
        publicar_imagem(args.imagem, args.legenda, ig_user_id, token, imgbb_key, scheduled_ts)

    elif args.tipo == "carrossel":
        if not args.pasta:
            print("ERRO: --pasta é obrigatório para --tipo carrossel", file=sys.stderr)
            sys.exit(1)
        publicar_carrossel(args.pasta, args.legenda, ig_user_id, token, imgbb_key, scheduled_ts)


if __name__ == "__main__":
    main()
