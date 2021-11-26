# Memulai project Web App dengan Python 3 & Django

Install Python 3.
Jika anda menggunakan sistem operasi berbasis Linux (e.g Ubuntu) maka secara default Python sudah terinstall di komputer anda.

Cek versi python
`python3 --version` 
Python 3.8.10

Install Pip3
`sudo apt update`
`sudo apt install python3-pip`
`pip3 --version`  
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

Sebelum memulai project, ada baiknya ada membuat sebuah virtual environment terlebih dahulu. 
Tujuan penggunaan virtual environment adalah untuk mengisolasi sebuah project agar package-package yang digunakan hanya terinstall di project tersebut saja dan tidak mengganggu project lain, ada bisa saja tidak menggunakan virtual environment apabila merasa ingin menggunakan semua package-package untuk semua project python anda (instalasi package python secara global).

Cara membuat sebuah virtual environment
Install package python3-venv
`sudo apt-get install python3-venv`

`mkdir project_django_web_app`
`cd project_django_web_app`
`python3 -m venv myenv`

aktivasi virtual environment
`source myenv/bin/activate` # ingat untuk selalu mengaktivasisebelum memulai development

Install Django Web Framework di dalam virtual environment
`pip install django`

anda dapat menspesifikan versi django yang akan anda install atau cukup dengan mengikuti contoh diatas untuk menggunakan Django versi terbaru

untuk melihat package-package apa saja yang sudah terinstal di dalam virtual environment dapat menggunakan perintah 
`pip3 list`

Membuat Django App Project
`django-admin startproject <nama_project>`

Menjalankan Django Web App pertama kali
cd <nama_project>
`python3 manage.py runserver`

`Stop runserver dengan CTRL+C`

Membuat sebuah App baru untuk Web App
`python3 manage.py startapp <nama_app>`

Membuat file `.env` untuk menyimpan confidential data
install package django-environ
`pip install django-environ`
gunakan untuk data confidential misalnya SECRET_KEY

Buat sebuah database menggunakan postgre.
`sudo -i -u postgres psql`      # masuk ke postgresql
`create database <nama_db>;`    # membuat database
`\c`                            # menghubungkan user postresql dengan database yg baru dibuat

Koneksi ke database postgresql
`pip install psycopg2-binary`   # disini kita masih menggunakan standalone atau pre-compiled binary version yg tidak membutuhkan build/runtime prerequisites

Setup pengaturan koneksi database di file settings.py
kemudian jalankan `python3 manage.py migrate` 

Buatlah model/table database yg anda ingininkan dalam file `models.py`
kemudian jalankan perintah `python3 manage.py makemigrations <nama_app>` 
kemudian jalankan `python3 manage.py migrate` lagi untuk mengeksekusi perintah yg sudah disiapkan dari langkah diatas

