# TUGAS 2

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*
Heroku app url : https://dinadatabaseapp.herokuapp.com/katalog/

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## (*) Flowchart

![Flowchart](https://user-images.githubusercontent.com/92242454/190170707-5d9d5051-96bd-4e8b-a826-cc60d609e63d.jpg)


## (*) Framework Explanation

1. Berawal dari permintaan client mengikuti pengaturan pada `setting.py` lalu permintaan tersebut mencapai URL router, yang menggunakan file `urls.py` sebagai variable 
   ```python
   from django.urls import path
   from katalog.views import show_catalog
   app_name = 'katalog'
   urlpatterns = [
      path('', show_catalog, name='show_catalog'),
   ]
   ```
2. Saat variable tersebut telah cocok, variable akan dikirim ke file `views.py` untuk mengatur variable views dan memanggil fungsi yang dibutuhkan
   ```python
   from django.shortcuts import render
   from katalog.models import CatalogItem
   def show_katalog(request):
    database_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': database_katalog,
        'Nama': 'Dina Dwi Kinanty 🌸',
        'NPM': '2106751650'
    }
    return render(request, "katalog.html", context)
   ```
   
3. Jika operasi mendeteksi ada aktivitas pada database, tampilan akan mengirimkan query ke file `models.py`:
   ```python
   from django.db import models
   class CatalogItem(models.Model):
      item_name = models.CharField(max_length=255)
      item_price = models.BigIntegerField()
      item_stock = models.IntegerField()
      description = models.TextField()
      rating = models.IntegerField()
      item_url = models.URLField()
   ```
Hal ini lalu akan dikirim ke database untuk memproses info yang diperlukan. File views akan menerima data berupa query. Views ini kemudian akan memilih HTML yang sesuai dengan yang telah atur sebelumnya. HTML ini lah yang akhirnya akan dilihat oleh client pada browser masing-masing sebagai hasil akhirnya.

## (*) Why Virtual Environment?

Virtual Environment merupakan sebuah ruang lingkup virtual yang terisolasi dari dependencies utama. Virtual Environment sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara satu project dengan lainnya yang berjalan pada operasi yang sama sehingga lebih mudah dalam menghindari error atau pertentangan antara operasi yang digunakan dengan operasi utama. Virtual environtment juga merupakan sebuah alat pengembang yang dianjurkan untuk sebuah project berbahasa komputasi python. Karena proyek-proyek ini memiliki kebutuhan/ketergantungan yang berbeda, kita memerlukan lingkungan virtual untuk menjalankannya tanpa mengubah konfigurasi sistem yang sedang kita gunakan. Selain itu Virtual Environment juga developer dalam melakukan mobilisasi project tanpa melakukan konfigurasi ulang.

Sedikit penjelasan mengenai Django itu sendiri, DDjango adalah sebuah framework full-stack untuk membuat aplikasi web dengan bahasa pemrograman Python. Framework akan membantu kita membuat web lebih cepat, dibandingkan menulis kode dari nol. Kegunaan Virtual Environtmen dalam aplikasi djanggo ada;ah sebaggai pembatas antar masing masing operasi dari sebuah project. Hal ini digunakan untuk mempermudah developer dalam mengerjakan tugasnya tanpa terjadi konflik dengan operasi utama project yang dikerjakan. Namun hal ini bukanlah kewajiban dalam proses pengembangannya. Django app dapat berjalan tanpa menggunakan bantuan framework khusus seperti Virtual Environtment. Akan tetapi hal itu akan menjadi tantangan di lingkungan dengan banyak proyek. Seperti yang ditunjukkan sebelumnya, mengaplikasikan Virtual Environtment akan memfasilitasi manajemen independen dari banyak proyek Django.


## (*) Implementation

1. Buatlah sebuah fungsi yang menerima parameter request `show_catalog`  dalam `views.py` dan mengembalikan render(request, "katalog.html"). Lalu lakukan import models ke dalam file views.py. Kamu akan menggunakan class tersebut untuk melakukan pengambilan data dari database.

```python 
def show_katalog(request):
    database_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': database_katalog,
        'Nama': 'Dina Dwi Kinanty 🌸',
        'NPM': '2106751650'
    }
    return render(request, "katalog.html", context)
```
```python
from django.shortcuts import render
from katalog.models import CatalogItem
```
2. Buatlah sebuah berkas di dalam folder aplikasi katalog bernama urls.py untuk me Lakukan routing terhadap fungsi `views.py` yang berada pada folder katalog dengan `urls.py` yang bertujuan untuk menampilkan halaman HTML pada browser yang kita gunakan.

``` python
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
3. Isilah bagian kode `context` pada `show_katalog` sesuai denggan data diri yang ingin ditampilkan pada laman browser. Lalu panggil fungsi query ke model database dan simpan hasil query tersebut ke dalam sebuah variabel.

```python
context = {
        'list_barang': database_katalog,
        'Nama': 'Dina Dwi Kinanty 🌸',
        'NPM': '2106751650'
    }
```

4. Tambahkan `context` ke file `katalog.html` untuk menampilan html 
```python
{% extends 'base.html' %}

 {% block content %}

  <h1>Lab 1 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{Nama}}</p>

  <h5>Student ID: </h5>
  <p>{{NPM}}</p>

  <table>
    <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for barang in list_barang %}
        <tr>
            <th>{{barang.item_name}}</th>
            <th>{{barang.item_price}}</th>
            <th>{{barang.item_stock}}</th>
            <th>{{barang.description}}</th>
            <th>{{barang.rating}}</th>
            <th>{{barang.item_url}}</th>
        </tr>
    {% endfor %}
    </table>

 {% endblock content %}
```
5. Selanjutnya, silakan lakukan add, commit, dan push perubahan yang sudah kamu lakukan untuk menyimpannya ke dalam repositori GitHub.
    
