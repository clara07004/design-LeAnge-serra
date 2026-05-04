"""
gerar-imagem.py — GPT Image 2 (gpt-image-1) via OpenAI API
Uso: python gerar-imagem.py "prompt" "saida.png" [aspect_ratio]
  aspect_ratio: square | portrait | landscape (default: square)
"""

import sys
import os
import base64
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Uso: python gerar-imagem.py \"prompt\" \"saida.png\" [aspect_ratio]")
        sys.exit(1)

    prompt = sys.argv[1]
    output_path = Path(sys.argv[2])
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "square"

    # Mapa de ratios para tamanhos suportados
    sizes = {
        "square":    "1024x1024",
        "portrait":  "1024x1536",
        "landscape": "1536x1024",
    }
    size = sizes.get(aspect_ratio, "1024x1024")

    # API key: variável de ambiente ou arquivo credentials/
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        key_file = Path(__file__).parent.parent.parent.parent / "credentials" / "openai_key.txt"
        if key_file.exists():
            api_key = key_file.read_text().strip()

    if not api_key:
        print("ERRO: OPENAI_API_KEY não encontrada.")
        print("Adicione em credentials/openai_key.txt ou defina a variável de ambiente.")
        sys.exit(2)

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        print(f"Gerando imagem ({size}) — pode demorar 60-180s...")

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size,
            quality="high",
            n=1,
            output_format="png",
        )

        # Resposta pode ser URL ou base64
        image_data = response.data[0]
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if hasattr(image_data, "b64_json") and image_data.b64_json:
            img_bytes = base64.b64decode(image_data.b64_json)
            output_path.write_bytes(img_bytes)
        elif hasattr(image_data, "url") and image_data.url:
            import urllib.request
            urllib.request.urlretrieve(image_data.url, output_path)
        else:
            print("ERRO: resposta sem imagem válida.")
            sys.exit(3)

        print(f"OK: {output_path}")

    except Exception as e:
        print(f"ERRO: {e}")
        sys.exit(4)

if __name__ == "__main__":
    main()
