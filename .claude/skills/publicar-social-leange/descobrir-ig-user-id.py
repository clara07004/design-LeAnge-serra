"""
descobrir-ig-user-id.py — Descobre o Instagram Business User ID vinculado ao token Meta.

Uso:
  python descobrir-ig-user-id.py

Lê o token de credentials/meta_access_token.txt e retorna o IG User ID
para salvar em credentials/meta_ig_user_id.txt.
"""

import sys
from pathlib import Path

import httpx

# Atualizar GRAPH_API_VERSION quando a Meta descontinuar a versão atual.
# Versões suportadas: https://developers.facebook.com/docs/graph-api/changelog
GRAPH_API_VERSION = "v22.0"
GRAPH_API = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

# Este script fica em .claude/skills/publicar-social-leange/ — 4 níveis abaixo da raiz
CREDENTIALS_DIR = Path(__file__).parent.parent.parent.parent / "credentials"


def ler_token() -> str:
    caminho = CREDENTIALS_DIR / "meta_access_token.txt"
    if not caminho.exists():
        print("ERRO: credentials/meta_access_token.txt não encontrado.", file=sys.stderr)
        sys.exit(2)
    valor = caminho.read_text(encoding="utf-8").strip()
    if not valor or valor.startswith("PREENCHER"):
        print("ERRO: credentials/meta_access_token.txt não foi preenchido.", file=sys.stderr)
        sys.exit(2)
    return valor


def main():
    token = ler_token()

    print("Buscando páginas vinculadas ao token...")
    resp = httpx.get(
        f"{GRAPH_API}/me/accounts",
        params={"access_token": token},
        timeout=15,
    )
    dados = resp.json()

    if "error" in dados:
        print(f"ERRO: {dados['error']['message']}", file=sys.stderr)
        print("\nVerifique se o token em credentials/meta_access_token.txt é válido e tem permissões de Instagram.", file=sys.stderr)
        sys.exit(3)

    paginas = dados.get("data", [])
    if not paginas:
        print("Nenhuma página encontrada. O token precisa estar vinculado a uma Página do Facebook com conta Instagram Business/Creator.", file=sys.stderr)
        sys.exit(3)

    print(f"\nPáginas encontradas ({len(paginas)}):")
    for i, p in enumerate(paginas):
        print(f"  [{i}] {p['name']} (ID: {p['id']})")

    # Para cada página, buscar a conta Instagram vinculada
    ig_accounts = []
    for p in paginas:
        page_token = p.get("access_token", token)
        resp2 = httpx.get(
            f"{GRAPH_API}/{p['id']}",
            params={"fields": "instagram_business_account", "access_token": page_token},
            timeout=15,
        )
        dados2 = resp2.json()
        ig = dados2.get("instagram_business_account")
        if ig:
            ig_accounts.append({"pagina": p["name"], "ig_id": ig["id"]})

    if not ig_accounts:
        print("\nNenhuma conta Instagram Business/Creator vinculada encontrada.", file=sys.stderr)
        print("Acesse business.facebook.com e vincule uma conta Instagram à sua Página.", file=sys.stderr)
        sys.exit(3)

    print(f"\nContas Instagram encontradas ({len(ig_accounts)}):")
    for a in ig_accounts:
        print(f"  Pagina: {a['pagina']} -> IG User ID: {a['ig_id']}")

    # Se só uma, salva automaticamente
    if len(ig_accounts) == 1:
        ig_id = ig_accounts[0]["ig_id"]
        caminho_saida = CREDENTIALS_DIR / "meta_ig_user_id.txt"
        caminho_saida.write_text(ig_id, encoding="utf-8")
        print(f"\nSalvo em credentials/meta_ig_user_id.txt")
    else:
        print("\nMais de uma conta encontrada. Salve manualmente o ID correto em credentials/meta_ig_user_id.txt")


if __name__ == "__main__":
    main()
