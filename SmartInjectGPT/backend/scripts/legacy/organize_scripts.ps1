# 📁 Tengeneza folders
$folders = @("injectors", "setup", "ai_tools", "legacy")
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Name $folder -Force | Out-Null
}

# 🔁 Hamisha inject-related
Move-Item -Force -Path "manual_inject.ps1", "response_parser.ps1" -Destination ".\injectors" -ErrorAction SilentlyContinue

# ⚙️ Hamisha setup
Move-Item -Force -Path "setup_inject_env.ps1" -Destination ".\setup" -ErrorAction SilentlyContinue

# 🤖 Hamisha AI + auto + smartgift scripts
Get-ChildItem -Path .. -Filter "*.ps1" | Where-Object {
    $_.Name -match "^ai_|^auto_|^smartgift_"
} | Move-Item -Destination ".\ai_tools" -Force

# 🗃️ Hamisha zilizosalia kwenye legacy
Get-ChildItem -Path .. -Filter "*.ps1" | Where-Object {
    $_.Name -notmatch "manual_inject|response_parser|setup_inject_env|^ai_|^auto_|^smartgift_"
} | Move-Item -Destination ".\legacy" -Force

Write-Host "`n✅ Scripts organized successfully!" -ForegroundColor Green
