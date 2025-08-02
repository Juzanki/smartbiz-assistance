# ============================================
# 📜 PowerShell Script: setup_alembic_config.ps1
# 🚀 Auto-generate alembic.ini (UTF-8 no BOM)
# ✅ Supports SmartBiz Assistance - Railway Ready
# ============================================

$alembicPath = "E:\SmartBiz_Assistance\backend\alembic.ini"

# ⚠️ Step 1: Delete old alembic.ini if exists
if (Test-Path $alembicPath) {
    Remove-Item -Force $alembicPath
    Write-Host "🧹 Old alembic.ini deleted."
}

# 🧾 Step 2: Define improved config content
$config = @"
# ===============================================
# 🚀 Alembic Configuration for SmartBiz Assistance
# 📦 Supports PostgreSQL + .env via env.py
# 🔐 Uses .env.production loaded from env.py
# ===============================================

[alembic]
script_location = backend/alembic
prepend_sys_path = .
version_path_separator = os
output_encoding = utf-8

[post_write_hooks]
hooks = black
black.type = console_scripts
black.entrypoint = black
black.options = -l 100 REVISION_SCRIPT_FILENAME

[loggers]
keys = root, sqlalchemy, alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

# ✅ NOTE:
# DO NOT set sqlalchemy.url here — it is overridden by env.py
# Example (for reference only):
# sqlalchemy.url = postgresql+psycopg2://user:pass@localhost:5432/dbname
"@

# 🧠 Step 3: Write file with clean UTF-8 (no BOM)
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$writer = New-Object System.IO.StreamWriter($alembicPath, $false, $utf8NoBom)
$writer.Write($config)
$writer.Close()

Write-Host "`n✅ alembic.ini written successfully with clean UTF-8 encoding.`n" -ForegroundColor Green
