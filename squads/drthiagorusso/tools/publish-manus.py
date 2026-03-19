#!/usr/bin/env python3
"""
publish-manus.py — Publicação de carrossel no Instagram @drthiagorusso via API Manus (MCP)

Uso:
    python3 publish-manus.py --images "slide-01.jpg,slide-02.jpg,..." --caption "legenda" [--dry-run]

Este script usa o manus-mcp-cli para publicar via Instagram MCP,
sem necessidade de tokens externos (INSTAGRAM_ACCESS_TOKEN, IMGBB_API_KEY).

Requer:
    - manus-mcp-cli configurado com servidor 'instagram'
    - Imagens em formato JPEG, 1080x1350px
    - Caption com máximo 2200 caracteres
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Publicar carrossel no Instagram @drthiagorusso via API Manus")
    parser.add_argument("--images", required=True, help="Caminhos das imagens separados por vírgula")
    parser.add_argument("--caption", required=True, help="Legenda do post (máx 2200 chars)")
    parser.add_argument("--dry-run", action="store_true", help="Simular publicação sem postar de fato")
    return parser.parse_args()


def upload_image_to_public_url(image_path: str) -> str:
    """
    Faz upload da imagem para o imgbb e retorna a URL pública.
    Usa o manus-upload-file para obter uma URL pública temporária.
    """
    print(f"  📤 Fazendo upload: {image_path}")
    result = subprocess.run(
        ["manus-upload-file", image_path],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Erro no upload de {image_path}: {result.stderr}")
    
    # Extrair URL do output
    lines = result.stdout.strip().split("\n")
    for line in lines:
        if line.startswith("http"):
            return line.strip()
    
    raise RuntimeError(f"URL pública não encontrada no output: {result.stdout}")


def create_instagram_post(media_items: list, caption: str, dry_run: bool = False):
    """
    Cria o post no Instagram via manus-mcp-cli.
    """
    if dry_run:
        print("\n🧪 DRY-RUN: Simulando publicação (sem postar de fato)")
        print(f"  Imagens: {len(media_items)} slides")
        print(f"  Caption: {caption[:100]}...")
        return {"dry_run": True, "media_count": len(media_items)}
    
    payload = {
        "type": "post",
        "caption": caption,
        "media": media_items
    }
    
    payload_json = json.dumps(payload)
    
    result = subprocess.run(
        ["manus-mcp-cli", "tool", "call", "create_instagram",
         "--server", "instagram",
         "--input", payload_json],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        raise RuntimeError(f"Erro na publicação via MCP: {result.stderr}")
    
    # Ler resultado do arquivo temporário
    output_lines = result.stdout.strip().split("\n")
    result_file = None
    for line in output_lines:
        if "/tmp/manus-mcp/" in line or "mcp_result_" in line:
            # Extrair caminho do arquivo
            parts = line.split()
            for part in parts:
                if "mcp_result_" in part:
                    result_file = part
                    break
    
    if result_file and os.path.exists(result_file):
        with open(result_file) as f:
            return json.load(f)
    
    return {"output": result.stdout}


def main():
    args = parse_args()
    
    print("\n" + "━" * 50)
    print("📲 Publisher — Dr. Thiago Russo Oftalmologia")
    print("   Instagram: @drthiagorusso")
    print("━" * 50)
    
    # Validar caption
    if len(args.caption) > 2200:
        print(f"❌ Caption muito longa: {len(args.caption)} chars (máx 2200)")
        sys.exit(1)
    
    # Processar lista de imagens
    image_paths = [p.strip() for p in args.images.split(",") if p.strip()]
    
    if len(image_paths) < 2:
        print(f"❌ Mínimo 2 imagens para carrossel (recebido: {len(image_paths)})")
        sys.exit(1)
    
    if len(image_paths) > 10:
        print(f"❌ Máximo 10 imagens para carrossel (recebido: {len(image_paths)})")
        sys.exit(1)
    
    # Verificar se os arquivos existem
    for path in image_paths:
        if not os.path.exists(path):
            print(f"❌ Arquivo não encontrado: {path}")
            sys.exit(1)
    
    print(f"\n📋 Resumo:")
    print(f"  Imagens: {len(image_paths)} slides")
    print(f"  Caption: {len(args.caption)} caracteres")
    print(f"  Modo: {'DRY-RUN 🧪' if args.dry_run else 'PUBLICAÇÃO REAL 🚀'}")
    
    print(f"\n🖼️ Imagens a publicar:")
    for i, path in enumerate(image_paths, 1):
        size = os.path.getsize(path) / 1024
        print(f"  {i}. {os.path.basename(path)} ({size:.0f} KB)")
    
    print(f"\n📝 Caption (primeiros 200 chars):")
    print(f"  {args.caption[:200]}...")
    
    if not args.dry_run:
        print("\n⚠️  ATENÇÃO: O post será publicado IMEDIATAMENTE no @drthiagorusso")
        confirm = input("  Digite 'PUBLICAR' para confirmar: ")
        if confirm.strip().upper() != "PUBLICAR":
            print("❌ Publicação cancelada pelo usuário.")
            sys.exit(0)
    
    # Fazer upload das imagens e obter URLs públicas
    print("\n📤 Fazendo upload das imagens...")
    media_items = []
    
    for i, path in enumerate(image_paths, 1):
        print(f"  [{i}/{len(image_paths)}] {os.path.basename(path)}")
        try:
            public_url = upload_image_to_public_url(path)
            media_items.append({
                "media_url": public_url,
                "type": "image",
                "alt_text": f"Slide {i} — @drthiagorusso"
            })
            print(f"    ✅ URL: {public_url[:60]}...")
        except Exception as e:
            print(f"    ❌ Erro: {e}")
            sys.exit(1)
    
    # Publicar no Instagram
    print("\n🚀 Publicando no Instagram @drthiagorusso...")
    try:
        result = create_instagram_post(media_items, args.caption, args.dry_run)
        
        print("\n" + "━" * 50)
        if args.dry_run:
            print("✅ DRY-RUN concluído com sucesso!")
            print(f"  Simulação: {len(media_items)} slides prontos para publicação")
        else:
            print("✅ Post publicado com sucesso!")
            print(f"  Resultado: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
        print("━" * 50 + "\n")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Erro na publicação: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
