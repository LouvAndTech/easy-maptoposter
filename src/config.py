"""Global configuration and path management."""

import os
import sys
from pathlib import Path

def get_base_path():
    """Get the base path for the application (handles PyInstaller)."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return Path(sys._MEIPASS)
    else:
        # Running as script
        return Path(__file__).parent.parent

def get_data_path():
    if getattr(sys, 'frozen', False):
        #If running as a PyInstaller executable, use an OS specific location for user data
        """Get path for user data (writable location)."""
        if sys.platform == 'win32':
            base = Path(os.environ.get('APPDATA', Path.home()))
        elif sys.platform == 'darwin':
            base = Path.home() / 'Library' / 'Application Support'
        else:
            base = Path(os.environ.get('XDG_DATA_HOME', Path.home() / '.local' / 'share'))
        
        data_dir = base / 'MapPosterGenerator'
        data_dir.mkdir(parents=True, exist_ok=True)
    else:
        #If running as a script, use the parent directory for user data
        """Get path for user data (writable location)."""
        data_dir = get_base_path()
    return data_dir

# Base directories
PROJECT_ROOT = get_base_path()
DATA_ROOT = get_data_path()

# Read-only directories (bundled with app)
THEMES_DIR = PROJECT_ROOT / "themes"
FONTS_DIR = PROJECT_ROOT / "fonts"

# Writable directories (user data)
CACHE_DIR = Path(os.environ.get("CACHE_DIR", DATA_ROOT / "cache"))
POSTERS_DIR = DATA_ROOT / "posters"

# Create writable directories
CACHE_DIR.mkdir(parents=True, exist_ok=True)
POSTERS_DIR.mkdir(parents=True, exist_ok=True)

# Constants
FILE_ENCODING = "utf-8"
MAX_POSTER_DIMENSION = 20  # inches
DEFAULT_DISTANCE = 18000  # meters
DEFAULT_THEME = "terracotta"
DEFAULT_WIDTH = 12  # inches
DEFAULT_HEIGHT = 16  # inches
