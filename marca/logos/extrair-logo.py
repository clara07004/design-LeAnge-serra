"""
Extrai logos do Google Drive e salva na pasta marca/logos/.

Uso: chamado pelo /setup durante a configuração inicial do projeto.
Requer MCP Google Drive configurado e IDs das pastas em _contexto/referencias.md.
"""

import base64
import os
import sys


def salvar_logo(b64_content: str, nome_arquivo: str, output_dir: str) -> str:
    """Decodifica base64 e salva como arquivo de imagem."""
    os.makedirs(output_dir, exist_ok=True)
    caminho = os.path.join(output_dir, nome_arquivo)
    dados = base64.b64decode(b64_content)
    with open(caminho, "wb") as f:
        f.write(dados)
    return caminho


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python extrair-logo.py <base64_content> <nome_arquivo>")
        print("Exemplo: python extrair-logo.py <b64> logo-cor.png")
        sys.exit(1)

    b64 = sys.argv[1]
    nome = sys.argv[2]
    output_dir = os.path.dirname(os.path.abspath(__file__))

    caminho = salvar_logo(b64, nome, output_dir)
    print(f"Salvo: {caminho} ({os.path.getsize(caminho)} bytes)")
