; Inno Setup Script for Map Poster Generator
[Setup]
AppName=Map Poster Generator
AppVersion=1.0.0
AppPublisher=Map Poster Generator
AppPublisherURL=https://github.com/yourusername/maptoposter
DefaultDirName={autopf}\MapPosterGenerator
DefaultGroupName=Map Poster Generator
OutputDir=dist
OutputBaseFilename=MapPosterGenerator-Setup
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
WizardStyle=modern

[Files]
Source: "dist\MapPosterGenerator\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Map Poster Generator"; Filename: "{app}\MapPosterGenerator.exe"
Name: "{autodesktop}\Map Poster Generator"; Filename: "{app}\MapPosterGenerator.exe"

[Run]
Filename: "{app}\MapPosterGenerator.exe"; Description: "Launch Map Poster Generator"; Flags: nowait postinstall skipifsilent
