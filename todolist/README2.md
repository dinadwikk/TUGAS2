# TUGAS 5

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

Heroku app url : https://dinaherokuver.herokuapp.com/todolist/

Nama  : Dina Dwi K.
NPM   : 2106751650
PBP   : PBP-B

# Pendahuluan
Pada tugas ini, kamu akan mengimplementasikan HTML, CSS, pengaturan static files pada Django, dan beberapa hal yang sudah dipelajari selama tutorial lab.

Cascading Style Sheets (CSS) adalah bahasa yang digunakan untuk mendeskripsikan tampilan dan format dari sebuah situs web yang ditulis pada markup language (seperti HTML). Kegunaannya menjadikan tampilan situs web lebih menarik.
Secara umum, CSS dapat dituliskan dalam bentuk sebagai berikut.
```
selector {
  properties: value;
}
```
Terdapat tiga jenis cara penulisan CSS:

- Inline Styles
- Internal Style Sheet
- External Style Sheet

# Perbedaan 3 jenis cara penulisan CSS

- Inline Style
Digunakan untuk menata elemen HTML tertentu. Tambahkan atribut gaya ke setiap tag HTML tanpa menggunakan selector.
  - Dapat memperbaiki atribut dengaan cepat
  - Kurang efektif waktu karena harus melakukan editing 1 persatu
  - Dapat merubah ukuran halaman
  
- Internal Style Sheet
Memiliki tag <style> di bagian <head> dokumen HTML.
  - Dapat menggunakan selector Class dan ID
  - Tidak perlu menggg-upload banyak file
  - Dapat memperbesar ukuran halaman 
  
  
- External Style Sheet
Dapat menautkan halaman web ke file eksternal yang ditulis terpisah dengan file HTML pada file ekstensi .css.
  - Style diterapkan dalam file HTML yang berbeda
  - Dapat menggunakan file .css yang sama untuk beberapa halaman web di CSS eksternal
  - Struktur kode akan terlihat lebih rapih
  - Dapat terjadi error saat di render
  
# Tag HTML5 
1. `<button` : Membuat button
2. `<section>` : Mendefinisikan section dokumen
3. `<head>` : Mendefinisikan head dokumen
4. `<form>` : Mendefinisikan form HTML
5. `<div>` : Mendifinisikan bagian dalam dokumen

# Tipe CSS selector
1. Elemen Selector
Element selector menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.

2. ID Selector
ID selector menggunakan ID pada tag sebagai selector-nya. Lalu diimplementasikan dengan diawali #

3. Class Selector
Class selector yang dapat digunakan untuk memperindah tampilan template HTML lalu diimpelmentasikan menggunakan format .[class_name] (diawali .)

# Implementasi

1. Masukkan link src bootstrap pada `base.html` bagian `head`
```
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```
dan pada bagian `<body>`
```
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```

2. Lakukan perubahan gaya tampilan sesuai keinginan dengan diawali `<style>` dengan bantuan bootstrap yang ada
3. Buat class baru class="card" pada todolist untuk membuat card 
4. Jalankan dan deploy aplikasi

