<div align="center">Palette Create</div>
<div align="center">
  <img src="https://github.com/ruslanlap/palette-create/blob/master/output/logo.svg?raw=true" alt="Palette Create Logo" width="200" />
</div>

A Python-based color palette generator that creates high-quality color scheme visualizations in both PNG and SVG formats.

## Docker Setup

You can also use Docker; it will be easy peasy!

# Table of Contents
1. [Palette Create](#-palette-create)
2. [Example Output](#️-example-output)
   1. [Input Example](#in)
   2. [Output Example](#out)
3. [Description](#-description)
4. [Features](#-features)
5. [Color Scheme](#-color-scheme)
6. [Requirements](#️-requirements)
7. [Installation](#-installation)
8. [Windows Users Note](#️--windows-users-note)
   1. [ConvertApi Setup](#convertapi)
9. [Usage](#-usage)
10. [Output Examples](#️-output-examples)
11. [File Structure](#-file-structure)
12. [Contributing](#-contributing)
13. [License](#-license)
14. [Acknowledgments](#-acknowledgments)
15. [Contact](#-contact)
16. [Version History](#-version-history)
17. [Author](#-author)

## 🖼️ Example Output

### Input Example
```python
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
```

### Output Example

**PNG**  
![example_color_palette.png](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.png)

**SVG**  
![example_color_palette.svg](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.svg)  
![example_dracula_color_palette.svg](https://github.com/ruslanlap/palette-create/blob/master/output/example_dracula_color_palette.svg)

---

## 📜 Description

This tool generates a professional color palette visualization based on the **Frappé color scheme**. It provides detailed color information, including **HEX codes, RGB values, and HSL representations**. The output can be generated in both high-resolution PNG (300 DPI) and scalable SVG formats.

---

## ✨ Features

- 🎨 High-quality color palette visualization
- 🖼️ Support for both PNG (300 DPI) and SVG output
- 📋 Complete color information display (HEX, RGB, HSL)
- 🧼 Clean, modern design with color preview circles
- 🖋️ Professional typography and layout
- 🌙 Dark theme interface

---

## 🎨 Color Scheme

The Frappé color scheme includes (customizable via **`colors []`**):

- **Base Colors**: 🌸 Rosewater, 🦩 Flamingo, 💗 Pink, 💜 Mauve, 🔴 Red, 🩸 Maroon, 🍑 Peach, 🌟 Yellow
- **Interface Colors**: 💚 Green, 🐟 Teal, 🌌 Sky, 🔷 Sapphire, 🔵 Blue, 💜 Lavender
- **Text and Surface Colors**: 📝 Text, 🪶 Subtext, ☁️ Overlay, 🖤 Surface, ⚪ Base, 🌑 Mantle, 🌋 Crust

---

## ⚙️ Requirements

- 🐍 Python 3.x
- 🖼️ Pillow (PIL) library
- 📝 ConvertApi library (optional)
- 🖌️ CairoSVG library

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/ruslanlap/palette-create.git
# Navigate to the project directory
cd palette-create
# Install required dependencies
pip install -U -r requirements.txt
```

## ⚠️ ⊞ Windows Users Note

If you're using Windows, you'll need to install the `cairosvg` library separately. You can do this through various methods such as 'GTK for Windows Runtime Installer', 'MSYS2', 'WSL', etc., but I offer you a simpler way: using the API tool called [ConvertApi](https://convertapi.com/). Follow the step-by-step guide below to set up ConvertApi.

### ConvertApi Setup

1. Go to [convertapi.com](https://convertapi.com/) and log in to get your API key.
2. Set your API key to an environment variable `YOUR_API_KEY` in the `.env` file.
3. Set up a virtual environment (`venv`).
4. Rename `requirements-windows.txt` to `requirements.txt`.
5. Run `pip install -r requirements.txt`.
6. Run `python main-windows.py --use-api` and enjoy.

ConvertApi is a free online service that allows you to convert files between different formats. You have a 250 usage file limit for one month during your trial period.

---

## 🚀 Usage

```bash
python -m venv venv
# Activate the virtual environment
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Unix or MacOS
# Install requirements
pip install -r requirements.txt
# Generate both formats
python main.py
# Generate PNG version
python main.py --png
# Generate SVG version
python main.py --svg
# Generate both formats
python main.py --png --svg
```

## 🚢 Docker Usage
FOR EXAMLE of create

```bash
docker pull ruslanlap/palette-creator:latest
```

And then
```bash
mkdir -p output && docker run --rm -v "$(pwd)/output:/app/output" ruslanlap/palette-creator
```
And now you can use it without any additional headaches`

You can pass your own color palette in the options. To do this, create a palette with a `.py` extension following this example:

```bash
docker pull ruslanlap/palette-creator:latest && mkdir -p output

# And final create your own palette 
docker run --rm \
  -v "$(pwd)/output:/app/output" \
  -v "$(pwd)/example.py:/app/example.py" \
  ruslanlap/palette-creator --palette /app/example.py
```
And now you can use it without any additional headaches

```python
colors = [
    ("Rosewater", "#f2d5cf", "rgb(242, 213, 207)", "hsl(10deg, 57%, 88%)"),
]
```

This means you need to define your custom colors in a similar format within a Python file and then provide the path to this file using the `--palette` argument when running the script."
If you need further assistance or more detailed instructions, feel free to ask!

```bash
docker run --rm -v $(pwd):/app palette-creator --palette example.py
```

---

## 🖼️ Output Examples

The generator creates two types of files:
- **`example_color_palette.png`** - High-resolution bitmap image (300 DPI)
- **`example_color_palette.svg`** - Scalable vector graphics file

---

## 📂 File Structure

```
palette-create/
├── main.py
├── README.md
└── output/
    ├── example_color_palette.png
    └── example_color_palette.svg
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 🛠️

---

## 📜 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🌟 Acknowledgments

- 🎨 Frappé color scheme inspiration from the beautiful 😍 Catppuccin theme.
- 🖼️ PIL library for image processing
- 📐 SVG standard for vector graphics

---

## 📧 Contact

- GitHub: [@ruslanlap](https://github.com/ruslanlap)

---

## 🕒 Version History

- **1.0.0** (2024-01-17)
  - Initial release
  - Support for PNG and SVG output
  - Complete Frappé color scheme implementation
  - Clean design with color preview circles
  - Professional typography and layout
  - Dark theme interface

---

## 👨‍💻 Author

[@ruslanlap](https://github.com/ruslanlap)