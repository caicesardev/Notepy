$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$appDirectory = Join-Path $projectRoot "app"
$distDirectory = Join-Path $projectRoot "dist"
$buildDirectory = Join-Path $projectRoot "build"
$version = (Select-String -Path (Join-Path $appDirectory "constants.py") -Pattern 'VERSION = "(.+)"').Matches[0].Groups[1].Value
$executableName = "Notepy-$version-windows-x64"

python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name $executableName `
    --icon (Join-Path $projectRoot "res\images\notes.ico") `
    --paths $appDirectory `
    --distpath $distDirectory `
    --workpath $buildDirectory `
    --specpath $buildDirectory `
    (Join-Path $appDirectory "main.py")

Write-Host "Build ready: $(Join-Path $distDirectory "$executableName.exe")"
