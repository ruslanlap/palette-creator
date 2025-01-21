import argparse
from PIL import Image, ImageDraw, ImageFont
import os
import cairosvg
from color_palette import colors


def create_svg_palette():
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1400" height="1800" xmlns="http://www.w3.org/2000/svg">
    <style>
        .title { font-size: 48px; font-family: Arial; fill: rgb(198, 208, 245); }
        .header { font-size: 32px; font-family: Arial; fill: rgb(165, 173, 206); }
        .text { font-size: 24px; font-family: Arial; fill: rgb(198, 208, 245); }
    </style>
    <rect width="100%" height="100%" fill="rgb(35, 38, 52)"/>
    <text x="120" y="80" class="title">Example Pallete</text>
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

    with open('example_color_palette.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

    return "example_color_palette.svg"

def convert_svg_to_png(svg_path, png_path):
    with open(svg_path, "rb") as svg_file:
        png_bytes = cairosvg.svg2png(file_obj=svg_file)
        with open(png_path, "wb") as png_file:
            png_file.write(png_bytes)

def main():
    parser = argparse.ArgumentParser(description='Generate color palette in PNG or SVG format')
    parser.add_argument('--svg', action='store_true', help='Generate SVG format only')
    args = parser.parse_args()

    # SVG is created first, PNG conversion follows if needed
    output_svg = create_svg_palette()
    if args.svg:
        print(f"SVG palette has been saved as {output_svg}")
    else:
        output_png = "example_color_palette.png"
        convert_svg_to_png(output_svg, output_png)
        print(f"PNG palette has been saved as {output_png}")

if __name__ == "__main__":
    main()