# 🎨 Palette Create

A Python-based color palette generator that creates high-quality color scheme visualizations in both PNG and SVG formats.

## 🖼️ Example Output

**PNG**  
![example_color_palette.png](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.png)

**SVG**  
![example_color_palette.svg](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.svg)

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

---

## 🚀 Usage

```bash
# Generate both formats
python main.py

# Generate PNG version
python main.py --png

# Generate SVG version
python main.py --svg

# Generate both formats
python main.py --png --svg
```

---

## 🖼️ Output Examples

The generator creates two types of files:

- **`frappe_color_palette.png`** - High-resolution bitmap image (300 DPI)
- **`frappe_color_palette.svg`** - Scalable vector graphics file

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

- 🎨 Frappé color scheme inspiration
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
