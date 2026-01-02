from palette_generator import MoodEngine
from utils import visualize_palette, save_palette

def run_examples():
    engine = MoodEngine()
    
    moods = ["sunset", "cyberpunk", "sad", "forest", "calm", "vibrant"]
    
    print("🎨 Chromatica: Mood-Driven Color Palette Generator")
    print("-" * 50)
    
    for mood in moods:
        print(f"Generating palette for mood: {mood}")
        
        # Scenario 1: Random palette
        palette1 = engine.generate_palette(mood)
        print(f"  Random: {palette1}")
        
        # Scenario 2: Reproducible palette with seed
        seed = 42
        palette2 = engine.generate_palette(mood, seed=seed)
        palette3 = engine.generate_palette(mood, seed=seed)
        
        print(f"  Seed {seed} (A): {palette2}")
        print(f"  Seed {seed} (B): {palette3}")
        
        # Verify reproducibility
        if palette2 == palette3:
            print("  ✅ Reproducibility verified.")
        else:
            print("  ❌ Reproducibility failed.")
        
        # Save as image
        save_palette(palette2, mood)
        
        # Display (this will open windows if run in a standard environment)
        # visualize_palette(palette2, mood)
        
    print("-" * 50)
    print("Done! Check the folder for .png files.")

if __name__ == "__main__":
    run_examples()
