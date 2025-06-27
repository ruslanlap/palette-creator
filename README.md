<div align="center">
  <img src="https://github.com/ruslanlap/palette-create/blob/master/output/logo.svg?raw=true" alt="Palette Creator Logo" width="200" />
  <h1>Palette Creator</h1>
</div>

A versatile Python-based tool for generating high-quality color palette visualizations in both PNG and SVG formats. Easily create and showcase your custom color schemes with detailed information including HEX, RGB, and HSL values.

---

## ✨ Features

-   🎨 **High-Quality Visualizations**: Generates professional color palette images.
-   🖼️ **Multiple Output Formats**: Supports both scalable SVG and high-resolution PNG (300 DPI) outputs.
-   📋 **Comprehensive Color Information**: Displays color names, HEX codes, RGB values, and HSL representations.
-   ⚙️ **Customizable Palettes**: Easily define and use your own color schemes via a simple Python file.
-   🧼 **Clean & Modern Design**: Features a sleek layout with color preview circles and professional typography.
-   🌙 **Dark Theme Interface**: Designed with a dark theme for comfortable viewing.
-   🐳 **Docker Support**: Run the generator seamlessly in a Docker container without local dependencies.

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### ⚙️ Requirements

-   Python 3.x
-   `cairosvg` (for SVG to PNG conversion)
-   `Pillow` (for image manipulation)
-   `argparse` (for command-line argument parsing)

### 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ruslanlap/palette-create.git
    cd palette-create
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Unix or MacOS:
    source venv/bin/activate
    ```

3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### ⚠️ Windows Users Note

If you're using Windows, installing `cairosvg` can be challenging due to its dependencies. A simpler alternative is to use the [ConvertAPI](https://convertapi.com/) service.

#### ConvertAPI Setup (Windows Alternative)

1.  Go to [convertapi.com](https://convertapi.com/) and log in to get your API key.
2.  Set your API key as an environment variable named `CONVERTAPI_SECRET` in a `.env` file in the project root.
3.  Install the Windows-specific requirements:
    ```bash
    pip install -r requirements-windows.txt
    ```
4.  Run the Windows-specific script:
    ```bash
    python main-windows.py --use-api
    ```
    ConvertAPI offers a free trial with a usage limit.

---

## 💡 Usage

The `main.py` script allows you to generate color palettes with various options.

### Default Usage (Generates SVG and PNG)

```bash
python main.py
```

### Generate Specific Formats

-   **Generate SVG only:**
    ```bash
    python main.py --svg
    ```
-   **Generate PNG only:**
    ```bash
    python main.py --png
    ```
-   **Generate both (explicitly):**
    ```bash
    python main.py --png --svg
    ```

### Using a Custom Color Palette

You can define your own color palette in a Python file (e.g., `my_palette.py`) and pass it to the script using the `--palette` argument. The file should contain a list named `colors` in the following format:

**`my_palette.py` example:**
```python
colors = [
    ("ColorName1", "#HEXCODE1", "rgb(R, G, B)", "hsl(H, S%, L%)"),
    ("ColorName2", "#HEXCODE2", "rgb(R, G, B)", "hsl(H, S%, L%)"),
    # ... more colors
]
```

**Run with custom palette:**
```bash
python main.py --palette my_palette.py
```

---

## 🐳 Docker Usage

You can also use Docker to run the Palette Creator without installing local dependencies.

### Pulling the Docker Image

```bash
docker pull ruslanlap/palette-creator:latest
```

### Running with Default Palette

This command will generate the default color palette and save the output to a local `output` directory.

```bash
mkdir -p output && docker run --rm -v "$(pwd)/output:/app/output" ruslanlap/palette-creator
```

### Running with a Custom Palette

To use your own color palette with Docker, mount your palette file into the container.

```bash
mkdir -p output
docker run --rm \
  -v "$(pwd)/output:/app/output" \
  -v "$(pwd)/my_palette.py:/app/my_palette.py" \
  ruslanlap/palette-creator --palette /app/my_palette.py
```
Replace `my_palette.py` with the actual path to your custom palette file.

---

## 🖼️ Example Output

The generator creates two types of files in the `output/` directory:

-   **`example_color_palette.png`**: High-resolution bitmap image (300 DPI)
-   **`example_color_palette.svg`**: Scalable vector graphics file

**PNG Example:**
![example_color_palette.png](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.png)

**SVG Example:**
![example_color_palette.svg](https://github.com/ruslanlap/palette-create/blob/master/output/example_color_palette.svg)
![example_dracula_color_palette.svg](https://github.com/ruslanlap/palette-create/blob/master/output/example_dracula_color_palette.svg)

---

## 📂 File Structure

```
palette-creator/
├── main.py                 # Main script for generating palettes
├── color_palette.py        # Default color palette definition
├── requirements.txt        # Python dependencies for general use
├── requirements-windows.txt# Python dependencies for Windows (ConvertAPI)
├── requirements-dev.txt    # Development dependencies (linting, testing)
├── example.env             # Example environment variables for ConvertAPI
├── README.md               # Project documentation
├── Docker/                 # Docker related files
│   ├── Dockerfile          # Dockerfile for building the image
│   └── ...                 # Other Docker related files
└── output/                 # Generated color palette images
    ├── example_color_palette.png
    └── example_color_palette.svg
    └── ...
```

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to submit a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.

---

## 🌟 Acknowledgments

-   🎨 Frappé color scheme inspiration from the beautiful Catppuccin theme.
-   🖼️ PIL library for image processing.
-   📐 SVG standard for vector graphics.
-   🐍 Python community for amazing tools and libraries.

---

## 📧 Contact

-   GitHub: [@ruslanlap](https://github.com/ruslanlap)

---

## 🕒 Version History

-   **1.0.1** (2025-06-27)
    -   Refactored `main.py` to accept custom palette files.
    -   Separated development dependencies into `requirements-dev.txt`.
    -   Updated `README.md` with detailed usage and project structure.
-   **1.0.0** (2024-01-17)
    -   Initial release
    -   Support for PNG and SVG output
    -   Complete Frappé color scheme implementation
    -   Clean design with color preview circles
    -   Professional typography and layout
    -   Dark theme interface