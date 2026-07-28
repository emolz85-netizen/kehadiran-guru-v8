SISTEM KEHADIRAN GURU SK ULU ANSUAN — VERSI 8.0
================================================

V8 menggunakan konfigurasi Render yang paling ringkas:

Build Command:
  pip install -r requirements.txt &&
  python manage.py collectstatic --noinput

Start Command:
  python manage.py migrate --noinput &&
  python manage.py create_initial_users &&
  gunicorn kehadiran_project.wsgi:application --bind 0.0.0.0:$PORT

Ciri:
- PostgreSQL lama melalui DATABASE_URL
- Akaun pentadbir dan guru automatik
- GPS radius 50 meter
- Kamera dan swafoto
- QR harian
- Import guru melalui Excel
- Cuti dan tugas rasmi
- Laporan PDF dan Excel
- PWA
- Health check

Baca LANGKAH_DEPLOY_V8.txt.
