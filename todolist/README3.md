# TUGAS 6

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

Heroku app url : https://dinaherokuver.herokuapp.com/todolist/create-ajax/

Nama  : Dina Dwi K.
NPM   : 2106751650
PBP   : PBP-B

# Penadahuluan Asynchronous pada AJAxx
Pada tugas ini, kita akan mengimplementasikan AJAX pada fungsionalitas todolist yang telah dibuat pada saat Tugas 4 dan 5. AJAX merupakan singkatan dari Asynchronous Javascript. 
Sehingga AJAX dapat melakukan running web secara asynchronous (tidak langsung). Dalam proses running programnya AJAX akan memunculkan running program secara pop-up sehingga tidak mengghilangkan page utama web. AJAX akan memproses setiap request (permintaan) yang datang ke server di sisi background.

# Perbedaan Asynchronous Programming & Synchronous Programming

| Asynchronous | Synchronous |
| ------------ | ----------- |
| Bekerja secara tidak langsung | Bekerja secara langsung|
| Program berjalan secara Sequential | Program dapat dijalankan secara bersamaan |
| Berjalan lebih cepat | Berjalan lebih lambat |

# Event-Driven Programming
 Suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Misal tombol 'tambah tugas' di klik makan akan muncul form pop up berupa pengisian detail tugas. Hal ini lah yang disebut event. 
 Pada tugas 6 kita menggunakan event driven programing sebagai implemntasi fungsi pada modul, sepert dibawah ini :
 ```
 $("#click").click(function(){
          $.post("http://127.0.0.1:8000/todolist/create-ajax/", "https://dinaherokuver.herokuapp.com/todolist/json/",{
            title : $('#title').val(),
            description: $('#description').val()},
            function (result)
            ....
  ```
  
  # Implementasi
  1. Buat fungsi JSON pada `views.py` lalu sambungkan pada path di `urls.py`
  2. Buat file `todolist_ajax.html` pada bagian ini kita akan menambhkan fungsi aja xpada html
  3. Terapkan atribut onClick dan sesuaikan dengan modal pada html
  4. Buat component card sebagai hasil akhir keluaran fungsi 
