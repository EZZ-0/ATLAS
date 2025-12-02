"""
Theme Presets for Atlas Financial Intelligence
"""

THEMES = {
    'blue_corporate': {
        'name': 'Blue Corporate (Current)',
        'primary': '#1e88e5',
        'primary_light': '#64b5f6',
        'primary_dark': '#0d47a1',
        'secondary': '#ffd700',
        'background': '#0a0e27',
        'surface': 'rgba(30, 136, 229, 0.15)',
        'text': '#ffffff',
        'gradient': 'linear-gradient(135deg, #1e88e5 0%, #ffd700 100%)',
    },
}

def get_theme(theme_name='blue_corporate'):
    return THEMES.get(theme_name, THEMES['blue_corporate'])

def get_theme_names():
    return {name: data['name'] for name, data in THEMES.items()}
