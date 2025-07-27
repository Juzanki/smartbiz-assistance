Write-Host "`n🚀 Starting SmartInjectGPT Backend on http://127.0.0.1:8010" -ForegroundColor Cyan
uvicorn backend.kernel.smartinject_kernel:app --host 127.0.0.1 --port 8010 --reload
