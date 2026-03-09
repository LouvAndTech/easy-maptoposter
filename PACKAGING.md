# Packaging Guide

This document explains how to package Map Poster Generator for distribution on Windows, Linux (Ubuntu/Debian), and macOS.

## Quick Start

### Local Build

```bash
# Make sure you're in your virtual environment
source .venv/bin/activate

# Run the build script
./build.sh
```

This will:
1. Install PyInstaller and dependencies
2. Build the executable using PyInstaller
3. Create a platform-specific package (DEB on Linux, DMG on macOS)

### GitHub Actions Build

To trigger an automated build for all platforms:

```bash
# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0
```

This will automatically:
- Build executables for Windows, Linux, and macOS
- Create installers (.exe, .deb, .dmg)
- Create a GitHub release with all packages attached

You can also manually trigger the workflow from the GitHub Actions tab.

## File Structure

```
maptoposter/
├── maptoposter.spec              # PyInstaller configuration
├── installer_windows.iss         # Inno Setup script for Windows installer
├── build.sh                      # Local build script
├── desktop/
│   └── maptoposter.desktop      # Linux desktop entry
├── icons/
│   ├── README.md                # Icon creation guide
│   ├── app_icon.ico             # Windows icon (create this)
│   ├── app_icon.icns            # macOS icon (create this)
│   └── app_icon.png             # Linux icon (create this)
└── .github/
    └── workflows/
        └── build-release.yml    # GitHub Actions workflow
```

## Prerequisites

### All Platforms
- Python 3.11+
- PyInstaller: `pip install pyinstaller`

### Linux (DEB package)
- Ruby and RubyGems: `sudo apt-get install ruby ruby-dev rubygems`
- FPM: `sudo gem install fpm`

### macOS (DMG)
- create-dmg: `brew install create-dmg`

### Windows (EXE installer)
- Inno Setup: Download from https://jrsoftware.org/isdl.php
- Or install via Chocolatey: `choco install innosetup`

## Platform-Specific Instructions

### Windows

1. **Build executable:**
   ```cmd
   pip install pyinstaller
   pyinstaller maptoposter.spec
   ```

2. **Create installer:**
   ```cmd
   choco install innosetup
   iscc installer_windows.iss
   ```

3. **Output:** `dist/MapPosterGenerator-Setup.exe`

### Linux (Ubuntu/Debian)

1. **Build executable:**
   ```bash
   pip install pyinstaller
   pyinstaller maptoposter.spec
   ```

2. **Create DEB package:**
   ```bash
   sudo gem install fpm
   ./build.sh
   ```

3. **Output:** `maptoposter_1.0.0_amd64.deb`

4. **Install:**
   ```bash
   sudo dpkg -i maptoposter_1.0.0_amd64.deb
   ```

### macOS

1. **Build app bundle:**
   ```bash
   pip install pyinstaller
   pyinstaller maptoposter.spec
   ```

2. **Create DMG:**
   ```bash
   brew install create-dmg
   ./build.sh
   ```

3. **Output:** `MapPosterGenerator.dmg`

## Application Data Locations

The packaged application uses platform-appropriate locations for user data:

### Windows
- Cache: `%APPDATA%\MapPosterGenerator\cache`
- Posters: `%APPDATA%\MapPosterGenerator\posters`

### Linux
- Cache: `~/.local/share/MapPosterGenerator/cache`
- Posters: `~/.local/share/MapPosterGenerator/posters`

### macOS
- Cache: `~/Library/Application Support/MapPosterGenerator/cache`
- Posters: `~/Library/Application Support/MapPosterGenerator/posters`

These directories are automatically created on first run.

## Configuration

### PyInstaller Spec File

The `maptoposter.spec` file configures:
- Entry point: `gui_launcher.py`
- Bundled data: `themes/`, `fonts/`
- Hidden imports for GUI libraries
- Platform-specific icons
- Console mode: disabled (GUI only)

### GitHub Actions Workflow

The workflow (`build-release.yml`) triggers on:
- Tags matching `v*` (e.g., `v1.0.0`)
- Manual dispatch from GitHub Actions tab

It builds on:
- `windows-latest` (Windows 11)
- `ubuntu-latest` (Ubuntu 22.04)
- `macos-latest` (macOS 12+)

## Troubleshooting

### Missing Icons
- See `icons/README.md` for icon creation instructions
- Builds will complete without icons (but won't look as polished)

### PyInstaller Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt -r requirements_gui.txt`
- Try a clean build: `rm -rf build dist && pyinstaller maptoposter.spec`

### Missing Modules at Runtime
- Add missing imports to `hiddenimports` in `maptoposter.spec`
- For data files, add to the `datas` list in `maptoposter.spec`

### GitHub Actions Fails
- Check the Actions tab for detailed logs
- Ensure all required files are committed (`desktop/`, `icons/`, etc.)
- Verify the repository has Actions enabled

## Testing

Before releasing:

1. **Test the executable locally:**
   ```bash
   ./build.sh
   ./dist/MapPosterGenerator/MapPosterGenerator
   ```

2. **Test the installer:**
   - Install the package
   - Run the installed application
   - Test creating a poster (cache and output should work)
   - Uninstall cleanly

3. **Verify data locations:**
   - Ensure cache and posters are written to user data directory
   - Themes and fonts are read from bundled resources

## Release Checklist

- [ ] Update version in `maptoposter.spec`, `installer_windows.iss`, and `build.sh`
- [ ] Create app icons (see `icons/README.md`)
- [ ] Test build locally on your platform
- [ ] Update CHANGELOG or release notes
- [ ] Commit all changes
- [ ] Create and push version tag: `git tag v1.0.0 && git push origin v1.0.0`
- [ ] Monitor GitHub Actions for successful build
- [ ] Download and test all platform packages
- [ ] Publish release notes on GitHub

## Version Management

To release a new version:

1. Update version numbers in:
   - `maptoposter.spec` (if displaying version)
   - `installer_windows.iss` (AppVersion)
   - GitHub Actions workflow (fpm -v parameter)

2. Create a git tag:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

3. GitHub Actions will automatically build and release

## Support

For issues with packaging:
- Check PyInstaller documentation: https://pyinstaller.org/
- Review GitHub Actions logs
- Ensure all dependencies are properly specified
