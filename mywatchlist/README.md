# TUGAS 3

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*
Heroku app url : https://dinawatchlist.herokuapp.com/mywatchlist/

Nama  : Dina Dwi K.
NPM   : 2106751650
PBP   : PBP-B

# Pendahuluan

Pada tugas ini, kita akan mengimplementasikan konsep data delivery serta beberapa hal yang sudah kamu pelajari selama tutorial lab. 
Data delivery adalah proses mentransfer data campaign dari platform Oracle Data Cloud menuju ke cookie. Lalu data campaign akan dikirimkan/ditransfer. Pengguna dapat mengoptimalkan data pada situs atau platform media yang dituju. 

# Perbedaan JSON, XML, dan HTML

#JSON
<img width="1417" alt="Screen Shot 2022-09-21 at 23 23 37" src="https://user-images.githubusercontent.com/92242454/191559285-33793205-95be-4b27-b7b8-0f0c7004add0.png">

- Json biasa digunakan dalam transfer dan penyimpanan data.
- Biasa ditulis dengan format text java script.
- Tidak dapat memproses data 
- Output data berupa JSON String.
- Data disimpan dalam bentuk tree structure.


# XML
<img width="745" alt="Screen Shot 2022-09-21 at 23 38 20" src="https://user-images.githubusercontent.com/92242454/191562053-765e3cda-c4f5-4b58-92fc-d16f1d06cb21.png">

- XML biasa digunakan dalam transfer dan penyimpanan data.
- Biasa ditulis dengan format bahasa markup.
- Dapat memproses document dan object.
- Output data berupa XML Document.
- Data disimpan dalam bentuk map dan key value.

# HTML
<img width="1011" alt="Screen Shot 2022-09-21 at 23 24 04" src="https://user-images.githubusercontent.com/92242454/191564354-59a673fa-6f0b-4810-aa64-29664b3458c6.png">

- HTML berfungsi untuk menampilkan data.
- Berupa bahasa markup
- HTML elements : <title> ... <title>
- Model DOM HTML dibangun sebagai tree of Objects.
  
# Mengapa perlu data delivery dalam pengimplementasian sebuah platform?
  
Dalam menampilkan sebuah data kita perlu menampilkannya dalam format HTML. Sebelum memasuki format HTML, data dapat disimpan dan di proses dalam bentuk XML atau JSON. Jika data yang inginkan dalam skala besar, maka akan sulit rasanya apabila harus menginput dan satu persatu. Maka dari itu data delivery dapat mempermudah developer untuk memindahkan, memproses, serta menampilkan data. Selain itu dengan menggunakan data delivery, kita dapat melakukan tukar informasi dalam sebuah platform.
  
# Implementasi Program
  
