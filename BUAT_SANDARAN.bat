@echo off
cd /d "%~dp0"
if not exist sandaran mkdir sandaran
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do set tarikh=%%d-%%b-%%c
for /f "tokens=1-2 delims=: " %%a in ("%time%") do set masa=%%a%%b
copy db.sqlite3 "sandaran\db_%tarikh%_%masa%.sqlite3"
echo Sandaran siap dalam folder sandaran.
pause
