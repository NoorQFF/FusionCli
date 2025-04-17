[Setup]
AppName=Fusion
AppVersion=1.0
DefaultDirName={autopf}\Fusion
DefaultGroupName=Fusion
OutputDir=dist-windows
OutputBaseFilename=fusion-installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\fusion.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Fusion"; Filename: "{app}\fusion.exe"

[Registry]
; Append {app}\ to PATH if not already there
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; \
    ValueData: "{olddata};{app}\"; Flags: preservestringtype

[Run]
Filename: "{app}\fusion.exe"; Description: "Launch Fusion"; Flags: nowait postinstall skipifsilent
