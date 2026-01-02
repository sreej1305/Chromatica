# 🎨 Chromatica — Mood-Driven Color Palette Generator

**Chromatica** is a pure Python tool that generates visually appealing color palettes based on mood or concept words (e.g., *sunset, cyberpunk, calm, forest*). It uses deterministic HSV logic to match colors to the specified theme.

## 🎯 Features
- 🌈 **Mood-Driven**: Maps words to specific Hue, Saturation, and Brightness profiles.
- ⚡ **Pure Python**: No heavy AI APIs or web frameworks.
- 📊 **Visualization**: Displays palettes using `matplotlib`.
- 💾 **Export**: Automatically saves palettes as `.png` images.
- 🧬 **Reproducible**: Supports random seeds for consistent generation.

## 🚀 Quick Start

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/sreej1305/Chromatica.git
cd Chromatica
pip install -r requirements.txt
```

### Usage
Run the examples script:
```bash
python examples.py
```

Or open the interactive notebook:
```bash
jupyter notebook chromatica.ipynb
```

## 🛠 File Structure
- `palette_generator.py`: Core logic for interpreting moods.
- `utils.py`: Conversion and visualization helpers.
- `chromatica.ipynb`: Interactive playground.
- `examples.py`: Batch generation demo.

## 🎨 Example Moods
- **Sunset**: Warm reds, oranges, and yellows.
- **Cyberpunk**: Neon pinks, purples, and electric blues.
- **Calm**: Soft teals and muted blues.
- **Forest**: Earthy greens and browns.

---
Built with ❤️ by [sreej1305](https://github.com/sreej1305)
