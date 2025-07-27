import zipfile
import os

# Paths and contents for each file
files_content = {
    "SmartDeployKit_2/injector.ps1": """
param (
    [string]$inputText,
    [string]$tag
)

# Soma ramani ya tags na files
$json = Get-Content -Path "tools/SmartDeployKit_2/file_map.json" -Raw | ConvertFrom-Json

# Tafuta target file kulingana na tag
$targetFile = $json.$tag

if (-not $targetFile) {
    Write-Host "❌ Tag [$tag] haijapatikana kwenye ramani."
    exit
}

$targetFilePath = "..\\..\\$targetFile"
if (-not (Test-Path $targetFilePath)) {
    New-Item -ItemType File -Path $targetFilePath -Force | Out-Null
    Add-Content $targetFilePath "`n# ==== GPT_INSERT_START [$tag] ===="
    Add-Content $targetFilePath "`n# ==== GPT_INSERT_END [$tag] ===="
}

$fileText = Get-Content -Path $targetFilePath -Raw
$startTag = "# ==== GPT_INSERT_START [$tag] ===="
$endTag = "# ==== GPT_INSERT_END [$tag] ===="
$pattern = "(?s)(?<=$startTag)(.*?)(?=$endTag)"

if ($fileText -match $pattern) {
    $existing = ($matches[0]).Trim()
    if ($existing -ne "") {
        Write-Host "⚠️ Code tayari ipo kwa [$tag], hakuna kilichowekwa."
        exit
    }
}

$updated = [regex]::Replace($fileText, $pattern, "`r`n$inputText`r`n")
Set-Content -Path $targetFilePath -Value $updated -Encoding UTF8
Write-Host "✅ Imeingizwa kwa mafanikio kwenye [$targetFile]"
""",

    "SmartDeployKit_2/file_map.json": """
{
    "backend:fibonacci": "backend/routes/ai_functions.py",
    "frontend:loginform": "frontend/src/components/LoginForm.vue",
    "backend:auth": "backend/auth.py"
}
""",

    "SmartDeployKit_2/smart_writer.py": """
import json
import os

def get_target_file(prompt):
    with open("file_map.json", "r") as f:
        mapping = json.load(f)
    for keyword, filepath in mapping.items():
        if keyword.lower() in prompt.lower():
            return filepath
    return "output.txt"
"""
}

# Create ZIP file
zip_path = "/mnt/data/SmartDeployKit.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for filepath, content in files_content.items():
        dir_name = os.path.dirname(filepath)
        os.makedirs(dir_name, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        zipf.write(filepath)
        os.remove(filepath)

zip_path
