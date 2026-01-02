import random
from utils import hsv_to_hex

class MoodEngine:
    """
    Interprets moods and generates color palettes based on Hue, Saturation, and Value (HSV).
    """
    
    # Predefined mood profiles: (Hue range, Saturation range, Value/Brightness range)
    # Hue: 0-1 (Red: 0, Green: 0.33, Blue: 0.66)
    # Saturation: 0-1
    # Value: 0-1
    MOODS = {
        "sunset": {
            "h_range": (0.0, 0.15),   # Reds, Oranges, Yellows
            "s_range": (0.6, 0.9),    # Vivid
            "v_range": (0.7, 1.0)     # Bright
        },
        "sad": {
            "h_range": (0.5, 0.7),    # Moody blues and purples
            "s_range": (0.1, 0.4),    # Muted/desaturated
            "v_range": (0.3, 0.5)     # Dark/dim
        },
        "cyberpunk": {
            "h_range": (0.7, 0.95),   # Pinks, Magentas, Purples, Electric Blues
            "s_range": (0.8, 1.0),    # Extremely saturated
            "v_range": (0.8, 1.0)     # Neon bright
        },
        "calm": {
            "h_range": (0.4, 0.6),    # Teals, soft blues, greens
            "s_range": (0.2, 0.5),    # Muted
            "v_range": (0.7, 0.9)     # Softly bright
        },
        "energetic": {
            "h_range": (0.05, 0.2),   # Yellows, Oranges
            "s_range": (0.8, 1.0),    # High saturation
            "v_range": (0.8, 1.0)     # Very bright
        },
        "vibrant": {
            "h_range": (0.0, 1.0),    # Anything
            "s_range": (0.8, 1.0),    # Highly saturated
            "v_range": (0.8, 1.0)     # Very bright
        },
        "forest": {
            "h_range": (0.25, 0.45),  # Deep greens to lime
            "s_range": (0.4, 0.8),    # Moderate
            "v_range": (0.2, 0.6)     # Earthy/darker
        },
        "ocean": {
            "h_range": (0.5, 0.65),   # Blues
            "s_range": (0.5, 1.0),    # Vivid
            "v_range": (0.4, 0.9)     # Varying depth
        },
        "minimalist": {
            "h_range": (0.0, 1.0),    # Any hue
            "s_range": (0.0, 0.1),    # Almost grayscale
            "v_range": (0.8, 1.0)     # Very light/airy
        }
    }

    def _get_profile(self, mood):
        mood = mood.lower()
        if mood in self.MOODS:
            return self.MOODS[mood]
        
        # Fallback logic for unknown moods: Default to neutral
        return {
            "h_range": (0.0, 1.0),
            "s_range": (0.1, 0.6),
            "v_range": (0.4, 0.8)
        }

    def generate_palette(self, mood, seed=None):
        """
        Generates 5 colors matching the mood's profile.
        Deterministic if seed is provided.
        """
        if seed is not None:
            random.seed(seed)
        
        profile = self._get_profile(mood)
        colors = []
        
        for _ in range(5):
            h = random.uniform(*profile["h_range"])
            s = random.uniform(*profile["s_range"])
            v = random.uniform(*profile["v_range"])
            colors.append(hsv_to_hex(h, s, v))
            
        return colors
