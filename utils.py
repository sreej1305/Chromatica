import colorsys
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def hsv_to_hex(h, s, v):
    """Converts HSV values (0-1) to HEX format."""
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )

def visualize_palette(colors, mood_word):
    """
    Displays the color palette using matplotlib.
    Each color is shown as a horizontal block with its HEX code.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Hide axes
    ax.set_axis_off()
    
    n_colors = len(colors)
    for i, color in enumerate(colors):
        # Create a rectangle for each color
        rect = patches.Rectangle((i / n_colors, 0), 1 / n_colors, 1, color=color)
        ax.add_patch(rect)
        
        # Determine text color based on brightness for readability
        # Simple heuristic: if V > 0.6, use dark text; else light text
        # (Though we are working with HEX here, so let's keep it simple)
        text_color = "white" if i % 2 == 0 else "black" 
        # Actually, let's just use white/black based on a rough luminance
        
        ax.text(
            (i + 0.5) / n_colors, 0.5, color.upper(),
            color="white", ha='center', va='center',
            fontsize=14, fontweight='bold',
            bbox=dict(facecolor='black', alpha=0.3, edgecolor='none', pad=2)
        )

    plt.title(f"Mood: {mood_word.capitalize()}", fontsize=18, pad=20, fontweight='bold')
    plt.tight_layout()
    plt.show()

def save_palette(colors, mood_word, filename=None):
    """Saves the palette as an image."""
    if filename is None:
        filename = f"{mood_word.lower()}_palette.png"
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_axis_off()
    n_colors = len(colors)
    for i, color in enumerate(colors):
        rect = patches.Rectangle((i / n_colors, 0), 1 / n_colors, 1, color=color)
        ax.add_patch(rect)
        ax.text(
            (i + 0.5) / n_colors, 0.5, color.upper(),
            color="white", ha='center', va='center',
            fontsize=14, fontweight='bold',
            bbox=dict(facecolor='black', alpha=0.3, edgecolor='none', pad=2)
        )
    plt.title(f"Mood: {mood_word.capitalize()}", fontsize=18, pad=20, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Palette saved as {filename}")
