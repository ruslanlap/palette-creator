import argparse
import importlib.util
from PIL import Image, ImageDraw, ImageFont
import os
import cairosvg

def load_palette_from_file(file_path):
    spec = importlib.util.spec_from_file_location("color_palette", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.colors  # Assuming colors is defined in color_palette.py

def create_svg_palette(colors):
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1400" height="1800" xmlns="http://www.w3.org/2000/svg">
    <style>
        .title { font-size: 48px; font-family: Arial; fill: rgb(198, 208, 245); }
        .header { font-size: 32px; font-family: Arial; fill: rgb(165, 173, 206); }
        .text { font-size: 24px; font-family: Arial; fill: rgb(198, 208, 245); }
    </style>
    <rect width="100%" height="100%" fill="rgb(35, 38, 52)"/>
    <text x="120" y="80" class="title">Example Palette</text>
    <text x="120" y="160" class="header">Color</text>
    <text x="420" y="160" class="header">Hex</text>
    <text x="720" y="160" class="header">RGB</text>
    <text x="1020" y="160" class="header">HSL</text>
'''
    y_position = 200
    for name, hex_code, rgb, hsl in colors:
        svg += f'''    <circle cx="100" cy="{y_position + 10}" r="15" fill="{hex_code}"/>
    <text x="140" y="{y_position + 20}" class="text">{name}</text>
    <text x="420" y="{y_position + 20}" class="text">{hex_code}</text>
    <text x="720" y="{y_position + 20}" class="text">{rgb}</text>
    <text x="1020" y="{y_position + 20}" class="text">{hsl}</text>
'''
        y_position += 60
    svg += '</svg>'
    output_svg = 'example_color_palette.svg'
    with open(output_svg, 'w', encoding='utf-8') as f:
        f.write(svg)
    return output_svg

def convert_svg_to_png(svg_path, png_path):
    with open(svg_path, "rb") as svg_file:
        png_bytes = cairosvg.svg2png(file_obj=svg_file)
        with open(png_path, "wb") as png_file:
            png_file.write(png_bytes)

def main():
    parser = argparse.ArgumentParser(description="Generate color palettes.")
    parser.add_argument('--svg', action='store_true', help='Generate SVG output')
    parser.add_argument('--png', action='store_true', help='Generate PNG output')
    parser.add_argument('--palette', type=str, help='Path to custom color palette file')

    args = parser.parse_args()

    if args.palette:
        colors = load_palette_from_file(args.palette)
    else:
        from color_palette import colors  # Default palette file

    output_svg = create_svg_palette(colors)

    if args.svg:
        print(f"SVG palette has been saved as {output_svg}")
    elif args.png:
        output_png = "example_color_palette.png"
        convert_svg_to_png(output_svg, output_png)
        print(f"PNG palette has been saved as {output_png}")
    else:
        print("No format specified, defaulting to PNG...")
        output_png = "example_color_palette.png"
        convert_svg_to_png(output_svg, output_png)
        print(f"PNG palette has been saved as {output_png}")

if __name__ == "__main__":
    main()