@echo off
chcp 65001 >nul
echo Starting IELTS Speaking Coach...
python3 "%~dp0main.py"
if %errorlevel%==99 exit
pause
