# Build all PDFs from documents/src/*.md
# Run from the repo root: .\documents\build-pdfs.ps1

$ErrorActionPreference = "Stop"

$SrcDir      = "$PSScriptRoot\src"
$OutDir      = "$PSScriptRoot\..\dist"
$Template    = "$SrcDir\resinsight-template.latex"
$Logo        = "$SrcDir\logo.png"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$LogoFlag = @()
if (Test-Path $Logo) {
    $logopath = $Logo -replace '\\', '/'
    $LogoFlag = @("--variable", "logopath=$logopath")
}

$Sources = Get-ChildItem -Path $SrcDir -Filter "*.md"

if ($Sources.Count -eq 0) {
    Write-Host "No .md files found in $SrcDir"
    exit 1
}

foreach ($src in $Sources) {
    $name = $src.BaseName
    $out  = "$OutDir\$name.pdf"
    Write-Host "Building $name.pdf ..."

    $args = @(
        $src.FullName,
        "--pdf-engine=xelatex",
        "--template=$Template",
        "--resource-path=$SrcDir;.",
        "--toc",
        "--variable", "mainfont=Georgia",
        "--variable", "sansfont=Arial",
        "--variable", "monofont=Cascadia Mono"
    ) + $LogoFlag + @("-o", $out)

    & pandoc @args
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to build $name.pdf"
    }
}

Write-Host ""
Write-Host "Done. PDFs written to: $OutDir"
