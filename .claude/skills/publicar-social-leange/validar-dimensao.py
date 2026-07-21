#!/usr/bin/env python3
"""
Valida que imagens (PNG/JPEG) têm EXATAMENTE a dimensão alvo do Instagram.

Uso:
    python validar-dimensao.py <arquivo_ou_pasta> [largura] [altura]

Padrão: 1080 x 1350 (feed Instagram retrato 4:5).
Lê as dimensões direto do header do arquivo — não depende de PIL/Pillow.

Saída: uma linha por imagem (OK / ERRO). Exit code 1 se qualquer imagem estiver fora
do alvo (para travar render/publicação). Exit code 0 se todas baterem.
"""
import sys, os, struct, glob


def png_size(data):
    # assinatura PNG (8 bytes) + IHDR: length(4)+'IHDR'(4)+width(4)+height(4)
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h = struct.unpack(">II", data[16:24])
    return w, h


def jpeg_size(data):
    if data[:2] != b"\xff\xd8":
        return None
    i = 2
    n = len(data)
    while i < n - 1:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        # SOF0..SOF15 (exceto DHT/JPG/DAC) carregam dimensões
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
        i += 2 + seg_len
    return None


def size_of(path):
    with open(path, "rb") as fh:
        data = fh.read()
    if path.lower().endswith(".png"):
        return png_size(data)
    if path.lower().endswith((".jpg", ".jpeg")):
        return jpeg_size(data)
    return None


def main():
    if len(sys.argv) < 2:
        print("uso: python validar-dimensao.py <arquivo_ou_pasta> [largura] [altura]")
        sys.exit(2)
    alvo = sys.argv[1]
    w_alvo = int(sys.argv[2]) if len(sys.argv) > 2 else 1080
    h_alvo = int(sys.argv[3]) if len(sys.argv) > 3 else 1350

    if os.path.isdir(alvo):
        # valida os PNGs finais (slide-*.png, post-*.png) — os arquivos publicáveis
        files = sorted(glob.glob(os.path.join(alvo, "slide-*.png")) +
                       glob.glob(os.path.join(alvo, "post-*.png")))
        if not files:
            files = sorted(glob.glob(os.path.join(alvo, "*.png")))
    else:
        files = [alvo]

    erros = 0
    for f in files:
        sz = size_of(f)
        if sz is None:
            print(f"?? nao consegui ler dimensao: {f}")
            erros += 1
            continue
        w, h = sz
        if (w, h) == (w_alvo, h_alvo):
            print(f"OK    {w}x{h}  {os.path.basename(f)}")
        else:
            print(f"ERRO  {w}x{h} (esperado {w_alvo}x{h_alvo})  {os.path.basename(f)}")
            erros += 1

    if erros:
        print(f"\n{erros} imagem(ns) FORA do padrao {w_alvo}x{h_alvo}. "
              f"NAO publicar/avancar — corrigir o HTML e re-renderizar.")
        sys.exit(1)
    print(f"\nTodas as {len(files)} imagem(ns) estao em {w_alvo}x{h_alvo}. OK para publicar.")
    sys.exit(0)


if __name__ == "__main__":
    main()
