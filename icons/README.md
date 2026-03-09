# Icons Directory

This directory should contain application icons for different platforms.

## Required Icon Files

To build packages for all platforms, you need to create the following icon files:

1. **app_icon.ico** (Windows)
   - Format: ICO
   - Recommended sizes: 16x16, 32x32, 48x48, 256x256
   - Used by Windows executable and installer

2. **app_icon.icns** (macOS)
   - Format: ICNS
   - Recommended size: 512x512 and 1024x1024
   - Used by macOS app bundle

3. **app_icon.png** (Linux)
   - Format: PNG
   - Recommended size: 256x256 or 512x512
   - Used by Linux desktop entry

## How to Create Icons

### Option 1: Online Converter
1. Create a high-resolution PNG image (512x512 or 1024x1024) with your app logo
2. Use a converter like:
   - https://cloudconvert.com/png-to-ico (for .ico)
   - https://cloudconvert.com/png-to-icns (for .icns)
   - Or https://iconverticons.com/ (converts to all formats)

### Option 2: Command Line Tools

#### For .ico (Windows):
```bash
# Using ImageMagick
convert app_icon.png -define icon:auto-resize=256,128,64,48,32,16 app_icon.ico
```

#### For .icns (macOS):
```bash
# Create iconset directory
mkdir app_icon.iconset
sips -z 16 16     app_icon.png --out app_icon.iconset/icon_16x16.png
sips -z 32 32     app_icon.png --out app_icon.iconset/icon_16x16@2x.png
sips -z 32 32     app_icon.png --out app_icon.iconset/icon_32x32.png
sips -z 64 64     app_icon.png --out app_icon.iconset/icon_32x32@2x.png
sips -z 128 128   app_icon.png --out app_icon.iconset/icon_128x128.png
sips -z 256 256   app_icon.png --out app_icon.iconset/icon_128x128@2x.png
sips -z 256 256   app_icon.png --out app_icon.iconset/icon_256x256.png
sips -z 512 512   app_icon.png --out app_icon.iconset/icon_256x256@2x.png
sips -z 512 512   app_icon.png --out app_icon.iconset/icon_512x512.png
sips -z 1024 1024 app_icon.png --out app_icon.iconset/icon_512x512@2x.png
iconutil -c icns app_icon.iconset
```

## Temporary Workaround

If you don't have icons ready yet, the build process will still work:
- The Windows and Linux builds will complete without icons
- The macOS build may show a default icon or fail the bundle step
- The application will still run correctly, just without a custom icon

You can add icons later and rebuild the packages.
