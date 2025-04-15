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
Source: "dist-windows\fusion.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Fusion"; Filename: "{app}\fusion.exe"

[Registry]
; Add the app's installation path to the PATH environment variable
Root: HKCU; Subkey: "Environment\Path"; ValueName: "Fusion"; ValueData: "{app}"; Flags: uninsdeletevalue

[Run]
; Optionally, you can launch the app after installation (optional)
Filename: "{app}\fusion.exe"; Description: "Launch Fusion"; Flags: nowait postinstall skipifsilent
