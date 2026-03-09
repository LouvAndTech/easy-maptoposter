#!/bin/bash
# Build script for Map Poster Generator

set -e

echo "Building Map Poster Generator..."

# Check if venv is activated, if not, activate it
if [[ -z "$VIRTUAL_ENV" ]]; then
    if [ -d ".venv" ]; then
        echo "Activating virtual environment..."
        source .venv/bin/activate
    fi
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements_gui.txt
pip install pyinstaller

# Build executable
echo "Building executable with PyInstaller..."
pyinstaller maptoposter.spec

# Platform-specific packaging
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Creating DEB package for Ubuntu/Debian..."
    
    # Check if fpm is installed
    if ! command -v fpm &> /dev/null; then
        echo "Installing fpm (requires sudo)..."
        sudo gem install --no-document fpm
    fi
    
    mkdir -p package/opt/maptoposter
    mkdir -p package/usr/share/applications
    mkdir -p package/usr/share/icons/hicolor/256x256/apps
    mkdir -p package/usr/bin
    
    cp -r dist/MapPosterGenerator/* package/opt/maptoposter/
    cp desktop/maptoposter.desktop package/usr/share/applications/
    
    # Copy icon if it exists
    if [ -f "icons/app_icon.png" ]; then
        cp icons/app_icon.png package/usr/share/icons/hicolor/256x256/apps/maptoposter.png
    fi
    
    # Create launcher script
    echo '#!/bin/bash' > package/usr/bin/maptoposter
    echo '/opt/maptoposter/MapPosterGenerator' >> package/usr/bin/maptoposter
    chmod +x package/usr/bin/maptoposter
    
    fpm -s dir -t deb -n maptoposter -v 1.0.0 \
        --description "Generate beautiful map posters for any city" \
        --license "MIT" \
        --category "Graphics" \
        -C package \
        opt usr
    
    echo "✓ DEB package created: maptoposter_1.0.0_amd64.deb"
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Creating DMG for macOS..."
    
    # Check if create-dmg is installed
    if ! command -v create-dmg &> /dev/null; then
        echo "Installing create-dmg..."
        brew install create-dmg
    fi
    
    create-dmg \
        --volname "Map Poster Generator" \
        --window-pos 200 120 \
        --window-size 800 400 \
        --icon-size 100 \
        --app-drop-link 600 185 \
        "MapPosterGenerator.dmg" \
        "dist/" || true
    
    echo "✓ DMG created: MapPosterGenerator.dmg"
    
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Windows executable created in dist/MapPosterGenerator/"
    echo "To create an installer, run Inno Setup with installer_windows.iss"
    echo "Or install Inno Setup and run: iscc installer_windows.iss"
fi

echo ""
echo "✓ Build complete!"
echo "Executable location: dist/MapPosterGenerator/"
