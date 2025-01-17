import argparse
import os
import sys
import convertapi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

    colors = [
        ("Rosewater", "#f2d5cf", "rgb(242, 213, 207)", "hsl(10deg, 57%, 88%)"),
            ("Flamingo", "#eebebe", "rgb(238, 190, 190)", "hsl(0deg, 59%, 84%)"),
            ("Pink", "#f4b8e4", "rgb(244, 184, 228)", "hsl(316deg, 73%, 84%)"),
            ("Mauve", "#ca9ee6", "rgb(202, 158, 230)", "hsl(277deg, 59%, 76%)"),
            ("Red", "#e78284", "rgb(231, 130, 132)", "hsl(359deg, 68%, 71%)"),
            ("Maroon", "#ea999c", "rgb(234, 153, 156)", "hsl(358deg, 66%, 76%)"),
            ("Peach", "#ef9f76", "rgb(239, 159, 118)", "hsl(20deg, 79%, 70%)"),
            ("Yellow", "#e5c890", "rgb(229, 200, 144)", "hsl(40deg, 62%, 73%)"),
            ("Green", "#a6d189", "rgb(166, 209, 137)", "hsl(96deg, 44%, 68%)"),
            ("Teal", "#81c8be", "rgb(129, 200, 190)", "hsl(172deg, 39%, 65%)"),
            ("Sky", "#99d1db", "rgb(153, 209, 219)", "hsl(189deg, 48%, 73%)"),
            ("Sapphire", "#85c1dc", "rgb(133, 193, 220)", "hsl(199deg, 55%, 69%)"),
            ("Blue", "#8caaee", "rgb(140, 170, 238)", "hsl(222deg, 74%, 74%)"),
            ("Lavender", "#babbf1", "rgb(186, 187, 241)", "hsl(239deg, 66%, 84%)"),
            ("Text", "#c6d0f5", "rgb(198, 208, 245)", "hsl(227deg, 70%, 87%)"),
            ("Subtext 1", "#b5bfe2", "rgb(181, 191, 226)", "hsl(227deg, 44%, 80%)"),
            ("Subtext 0", "#a5adce", "rgb(165, 173, 206)", "hsl(228deg, 29%, 73%)"),
            ("Overlay 2", "#949cbb", "rgb(148, 156, 187)", "hsl(228deg, 22%, 66%)"),
            ("Overlay 1", "#838ba7", "rgb(131, 139, 167)", "hsl(227deg, 17%, 58%)"),
            ("Overlay 0", "#737994", "rgb(115, 121, 148)", "hsl(229deg, 13%, 52%)"),
            ("Surface 2", "#626880", "rgb(98, 104, 128)", "hsl(228deg, 13%, 44%)"),
            ("Surface 1", "#51576d", "rgb(81, 87, 109)", "hsl(227deg, 15%, 37%)"),
            ("Surface 0", "#414559", "rgb(65, 69, 89)", "hsl(230deg, 16%, 30%)"),
            ("Base", "#303446", "rgb(48, 52, 70)", "hsl(229deg, 19%, 23%)"),
            ("Mantle", "#292c3c", "rgb(41, 44, 60)", "hsl(231deg, 19%, 20%)"),
            ("Crust", "#232634", "rgb(35, 38, 52)", "hsl(229deg, 20%, 17%)")
    ]

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

def convert_svg_with_api(svg_path, output_dir='.'):
    api_key = os.getenv('YOUR_API_KEY')
    if not api_key:
        print("Error: API key not found in .env file")
        sys.exit(1)
    print(f"Using API key: {api_key}")
    print(f"Converting file: {os.path.abspath(svg_path)}")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    convertapi.api_credentials = api_key
    
    # Convert to PNG using ConvertAPI
    try:
        result = convertapi.convert('png', {
            'File': svg_path
        }, from_format='svg')
        
        # Get the result file URL
        file_url = result.response['Files'][0]['Url']
        print(f"Converted file URL: {file_url}")
        
        # Download the file using requests
        import requests
        response = requests.get(file_url)
        if response.status_code == 200:
            output_path = os.path.join(output_dir, 'example_color_palette.png')
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved PNG to: {output_path}")
        else:
            print(f"Failed to download PNG file. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

def convert_svg_to_png(svg_path, png_path, use_api=False):
    if use_api:
        convert_svg_with_api(svg_path)
    else:
        print("Error: Local conversion requires Cairo library. Please install it or use --use-api option.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate color palette in PNG or SVG format')
    parser.add_argument('--svg', action='store_true', help='Generate SVG format only')
    parser.add_argument('--use-api', action='store_true', help='Use ConvertAPI for conversion')
    args = parser.parse_args()

    # SVG is created first, PNG conversion follows if needed
    output_svg = create_svg_palette()
    if args.svg:
        print(f"SVG palette has been saved as {output_svg}")
    else:
        output_png = "example_color_palette.png"
        convert_svg_to_png(output_svg, output_png, args.use_api)
        print(f"PNG palette has been saved as {output_png}")

if __name__ == "__main__":
    main()