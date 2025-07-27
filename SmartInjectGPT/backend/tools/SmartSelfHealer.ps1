# SmartSelfHealer.ps1 — Emergency Self-Healing Protocol for SmartInjectGPT

Write-Host "`n🛡️ SmartInjectGPT: Self-Healing Mode Activated..." -ForegroundColor Cyan

# Check logs for critical failures
$logPath = "$PSScriptRoot\..\result_log.txt"
if (!(Test-Path $logPath)) {
    Write-Host "⚠️ Hakuna log ya matokeo kupatikana." -ForegroundColor Yellow
    exit
}

$log = Get-Content $logPath -Raw
if ($log -match "ROLLBACK|EMERGENCY|CRITICAL") {
    Write-Host "❌ Tatizo kubwa limegunduliwa. Kuanza kujiponya..." -ForegroundColor Red

    # Step 1: Activate AI Self-Shield (lock system)
    python "..\defense\ai_self_shield.py"

    # Step 2: Attempt rollback using PatchRollback
    python "..\defense\auto_patch_rollback.py"

    # Step 3: Run full integrity + soul check
    python "..\security\integrity_guard.py"
    python "..\identity\soul_signature.py"

    # Step 4: Optional Resurrection
    python "..\core\resurrector.py"

    Write-Host "`n✅ SmartInjectGPT imemaliza kujiponya." -ForegroundColor Green
}
else {
    Write-Host "✅ Mfumo uko salama. Hakuna tatizo la dharura." -ForegroundColor Green
}
