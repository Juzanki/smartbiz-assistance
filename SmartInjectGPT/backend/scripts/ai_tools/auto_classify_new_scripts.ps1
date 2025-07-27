# ========================================
# Smart Auto Classifier for .ps1 scripts
# ========================================

$folders = @("injectors", "setup", "ai_tools", "legacy")
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Name $folder -Force | Out-Null
}

Get-ChildItem -Path . -Filter "*.ps1" | ForEach-Object {
    $fileName = $_.Name

    if ($fileName -match "^manual_inject|^response_parser") {
        Move-Item -Force -Path $_.FullName -Destination ".\injectors"
    }
    elseif ($fileName -match "^setup_inject_env") {
        Move-Item -Force -Path $_.FullName -Destination ".\setup"
    }
    elseif ($fileName -match "^ai_|^auto_|^smartgift_") {
        Move-Item -Force -Path $_.FullName -Destination ".\ai_tools"
    }
    elseif ($fileName -ne "auto_classify_new_scripts.ps1") {
        Move-Item -Force -Path $_.FullName -Destination ".\legacy"
    }
}

Write-Host "`n✅ Auto classification complete!" -ForegroundColor Cyan
