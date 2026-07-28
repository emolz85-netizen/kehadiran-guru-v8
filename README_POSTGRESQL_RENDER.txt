SISTEM KEHADIRAN GURU V5 — POSTGRESQL + RENDER + HTTPS
======================================================

PAKEJ INI SUDAH DISEDIAKAN UNTUK:
- Django
- PostgreSQL
- Render Blueprint
- HTTPS automatik
- Kamera dan GPS telefon
- PWA
- Gunicorn
- WhiteNoise untuk fail statik

PERKARA PENTING
---------------
ChatGPT tidak boleh menerbitkan aplikasi terus ke akaun Render/GitHub anda
tanpa anda log masuk dan memberi akses pada akaun tersebut.

LANGKAH PENERBITAN
------------------
1. Cipta akaun GitHub.
2. Cipta repository baharu.
3. Muat naik semua kandungan folder projek ini ke repository tersebut.
4. Log masuk ke Render.
5. Pilih New > Blueprint.
6. Sambungkan repository GitHub.
7. Render akan membaca render.yaml dan mencipta:
   - Web service Django
   - Pangkalan data PostgreSQL
8. Tunggu status menjadi Live.
9. Buka alamat HTTPS yang diberikan oleh Render.
10. Cipta akaun pentadbir melalui Render Shell:
      python manage.py createsuperuser

KOORDINAT SEKOLAH
-----------------
Semak nilai dalam render.yaml:
  SCHOOL_LATITUDE
  SCHOOL_LONGITUDE
  SCHOOL_RADIUS_METERS

Jika koordinat anda berbeza, ubah nilainya sebelum upload ke GitHub
atau edit Environment Variables dalam Render Dashboard.

KAMERA DAN GPS
--------------
Kamera dan GPS telefon memerlukan:
- alamat HTTPS
- kebenaran kamera
- kebenaran lokasi
- GPS telefon diaktifkan

Render menyediakan alamat HTTPS selepas deploy berjaya.

CATATAN PELAN
-------------
Pelan percuma boleh mempunyai had, tidur selepas tidak digunakan,
atau perubahan polisi. Untuk kegunaan rasmi sekolah, gunakan pelan
yang mempunyai prestasi dan pangkalan data berterusan yang sesuai.

KESELAMATAN
-----------
- Jangan gunakan akaun demo pada sistem awam.
- Gunakan kata laluan pentadbir yang kuat.
- Pastikan DJANGO_DEBUG=False.
- Jangan kongsi DATABASE_URL.
