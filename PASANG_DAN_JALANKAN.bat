@echo off
title Sistem Kehadiran Guru v5.0 SQLite
cd /d "%~dp0"

echo ==================================================
echo SISTEM KEHADIRAN GURU V5 - UJIAN TEMPATAN
echo SQLITE - TANPA MYSQLCLIENT / C++ BUILD TOOLS
echo ==================================================
echo.

if not exist .env (
  copy .env.example .env >nul
  echo Fail .env telah dicipta.
)

echo [1/5] Mengemas kini pip...
py -m pip install --upgrade pip
if errorlevel 1 goto ralat

echo [2/5] Memasang pakej aplikasi...
py -m pip install --only-binary=:all: -r requirements.txt
if errorlevel 1 (
  echo.
  echo Cuba pemasangan biasa...
  py -m pip install -r requirements.txt
  if errorlevel 1 goto ralat
)

echo [3/5] Menyediakan pangkalan data SQLite...
py manage.py makemigrations attendance
if errorlevel 1 goto ralat
py manage.py migrate
if errorlevel 1 goto ralat

echo [4/5] Menyediakan akaun demo...
py manage.py seed_demo
if errorlevel 1 goto ralat

echo [5/5] Membuka aplikasi...
echo.
echo Komputer:
echo http://127.0.0.1:8000
echo.
echo Telefon pada Wi-Fi yang sama:
echo Gunakan IPv4 komputer, contoh http://192.168.1.20:8000
echo.
start "" http://127.0.0.1:8000
py manage.py runserver 0.0.0.0:8000
exit /b

:ralat
echo.
echo PEMASANGAN GAGAL.
echo Ambil gambar bahagian ralat merah dan hantar kepada ChatGPT.
pause
