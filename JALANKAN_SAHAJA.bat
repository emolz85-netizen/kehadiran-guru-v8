@echo off
title Sistem Kehadiran Guru v5.0 SQLite
cd /d "%~dp0"
start "" http://127.0.0.1:8000
py manage.py runserver 0.0.0.0:8000
pause
