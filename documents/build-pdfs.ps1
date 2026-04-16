# Build all PDFs from documents/src/**/*.md
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

$Sources = Get-ChildItem -Path $SrcDir -Filter "*.md" -File -Recurse

if ($Sources.Count -eq 0) {
    Write-Host "No .md files found in $SrcDir"
    exit 1
}

$nameCounts = @{}

foreach ($src in $Sources) {
    $relativeSource = Resolve-Path -LiteralPath $src.FullName -Relative
    $safeName = $src.BaseName
    if ($nameCounts.ContainsKey($safeName)) {
        $nameCounts[$safeName] += 1
        $safeName = "$safeName_$($nameCounts[$safeName])"
    } else {
        $nameCounts[$safeName] = 1
    }
    $out  = Join-Path $OutDir "$safeName.pdf"
    Write-Host "Building $relativeSource -> $out"

    $resourcePath = "$($src.DirectoryName);$SrcDir;."

    $args = @(
        $src.FullName,
        "--pdf-engine=xelatex",
        "--template=$Template",
        "--resource-path=$resourcePath",
        "--toc",
        "--variable", "mainfont=Georgia",
        "--variable", "sansfont=Arial",
        "--variable", "monofont=Cascadia Mono"
    ) + $LogoFlag + @("-o", $out)

    & pandoc @args
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to build $safeName.pdf"
    }
}

Write-Host ""
Write-Host "Done. PDFs written to: $OutDir"
