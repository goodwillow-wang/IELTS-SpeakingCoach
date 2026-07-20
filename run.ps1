$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8
Write-Host "Starting IELTS Speaking Coach..." -ForegroundColor Green
python3 "$PSScriptRoot\main.py"
