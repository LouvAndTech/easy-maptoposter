# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

block_cipher = None

# Collect all data files
datas = [
    ('themes', 'themes'),
    ('fonts', 'fonts'),
]

# Collect hidden imports
hiddenimports = [
    'PyQt6.QtCore',
    'PyQt6.QtGui',
    'PyQt6.QtWidgets',
    'matplotlib',
    'matplotlib.backends.backend_agg',
    'osmnx',
    'geopandas',
    'shapely',
    'shapely.geometry',
    'requests',
    'PIL',
    'PIL._tkinter_finder',
]

# Add matplotlib data files
datas += collect_data_files('matplotlib')

# Add osmnx and geopandas data files (including package metadata)  
datas += collect_data_files('osmnx')
datas += collect_data_files('geopandas')

# OSMnx calls importlib.metadata.version("osmnx") at import time.
# Bundle distribution metadata explicitly so frozen builds can resolve it.
datas += copy_metadata('osmnx')

a = Analysis(
    ['gui_launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MapPosterGenerator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons/app_icon.ico' if sys.platform == 'win32' else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MapPosterGenerator',
)

# macOS app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name='MapPosterGenerator.app',
        icon='icons/app_icon.icns',
        bundle_identifier='com.maptoposter.app',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSHighResolutionCapable': 'True',
        },
    )
