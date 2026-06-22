"""
Extrai fotos de produto do Google Drive e salva na pasta dados/fotos-produto-preview/.

Uso: chamado pelo /setup ou manualmente para popular o preview de fotos.
Requer MCP Google Drive configurado e ID da pasta em _contexto/referencias.md.
"""

import base64
import os
import re
import sys


def salvar_foto(b64_content: str, titulo: str, output_dir: str, indice: int) -> str:
    """Decodifica base64 e salva como arquivo de imagem."""
    os.makedirs(output_dir, exist_ok=True)
    safe_title = re.sub(r"[^a-zA-Z0-9\-_]", "-", titulo)[:40]
    caminho = os.path.join(output_dir, f"{indice:02d}-{safe_title}.jpg")
    dados = base64.b64decode(b64_content)
    with open(caminho, "wb") as f:
        f.write(dados)
    return caminho


if __name__ == "__main__":
    # Usar via MCP Drive: baixar arquivos da pasta de fotos configurada
    # em _contexto/referencias.md → "Fotos do Produto" e chamar salvar_foto().
    print("Configure o ID da pasta em _contexto/referencias.md e use o MCP Google Drive.")
    print("Função salvar_foto() disponível para uso programático.")
