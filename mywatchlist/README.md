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
<img width="450" alt="Screen Shot 2022-09-21 at 23 24 04" src="https://user-images.githubusercontent.com/92242454/191564354-59a673fa-6f0b-4810-aa64-29664b3458c6.png">

- HTML berfungsi untuk menampilkan data.
- Berupa bahasa markup
- HTML elements : <title> ... <title>
- Model DOM HTML dibangun sebagai tree of Objects.
  
# Mengapa perlu data delivery dalam pengimplementasian sebuah platform?
  
Dalam menampilkan sebuah data kita perlu menampilkannya dalam format HTML. Sebelum memasuki format HTML, data dapat disimpan dan di proses dalam bentuk XML atau JSON. Jika data yang inginkan dalam skala besar, maka akan sulit rasanya apabila harus menginput dan satu persatu. Maka dari itu data delivery dapat mempermudah developer untuk memindahkan, memproses, serta menampilkan data. Selain itu dengan menggunakan data delivery, kita dapat melakukan tukar informasi dalam sebuah platform.
  
# Implementasi Program
  1. Buat suatu aplikasi baru bernama `mywatchlist` di proyek Django Tugas 2 pekan lalu
  2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah kamu buat ke dalam proyek Django-mu. Contohnya adalah sebagai berikut. 
  ```
  INSTALLED_APPS = [
    .....,
    'mywatchlist',
]
  ```
  3. Buka file `models.py` yang ada di folder `mywatchlist` dan tambahkan potongan kode berikut.
  ```
  class ContentMyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
  ```
  4. Lakukan perintah `python manage.py makemigrations' lalu lakukan python `manage.py migrate` untuk mempersiapkan migrasi dan menerapkan skema model ke dalam database Django lokal.
  5. Buatlah sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `initial_mywatchwishlist_data.json` yang berisi dengan kode dari data film berupa watched, title, rating, release date, dan juga review seperti berikut ini 
  ```
  [
    {
        "model":"mywatchlist.ContentMyWatchList",
        "pk":1,
        "fields":{
            "watched":"True",
            "title":"The Batman",
            "rating": "7.9",
            "release_date": "March 4, 2022",
            "review": "Good but not so good."
        }
},
    {
    "model":"mywatchlist.ContentMyWatchList",
    "pk":2,
    "fields":{
        "watched":"True",
        "title":"Spider-Man: No Way Home",
        "rating": "8.3",
        "release_date": "December 17, 2021",
        "review": "Just Awesome!"
    }
},
  ...
  ]
  ```
  6. Load data dengan perintah `python manage.py loaddata initial_wishlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal
  7. Pada bagian `views.py` yang ada pada folder `mywatchlist`,  buatlah sebuah fungsi untuk menerima parameter request JSON, HTML, XML dan mengembalikan render
  ```
  def show_html(request):
    ....
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = ContentMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = ContentMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
  8.Buat folder `templates` di dalam folder `mywatchlist` lalu tambahkan kode html sebagai berikut
  ```
  {% extends 'base.html' %}

{% block content %}

<h1>My Watch List - Tugas 3 PBP</h1>

<h4>Name: </h4>
<p>{{nama}}</p>

<h4>Student ID: </h4>
<p>{{id}}</p>

<table>
  <tr>
    <th>Watched</th>
    <th>Title</th>
    <th>Rating</th>
    <th>Release Date</th>
    <th>Review</th>
  </tr>
  {% comment %} Add the data below this line {% endcomment %}
  {% for film in data_film %}
      <tr>
          <th>{{film.watched}}</th>
          <th>{{film.title}}</th>
          <th>{{film.rating}}</th>
          <th>{{film.release_date}}</th>
          <th>{{film.review}}</th>
      </tr>
  {% endfor %}
</table>

 {% endblock content %}
  ```
  9. Daftarkan  aplikasi `mywatchlist` dalam `urls.py` 
  ```
  urlpatterns = [
   ...
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
   ...
]
  ```
  10. Jalankan aplikasi dengan `python manage.py runserver` lalu buka `http://localhost:8000/mywatchlist/` aplikasi siap digunakan
  
  # POSTMAN
  <img width="420" alt="Screen Shot 2022-09-21 at 14 38 53" src="https://user-images.githubusercontent.com/92242454/191639679-bd835d01-08f5-4f6c-bafe-0300b5efc8da.png">
<img width="418" alt="Screen Shot 2022-09-21 at 14 38 43" src="https://user-images.githubusercontent.com/92242454/191639693-644e038c-2db1-403f-a3fb-33c2d6627c4c.png">
<img width="419" alt="Screen Shot 2022-09-21 at 14 38 28" src="https://user-images.githubusercontent.com/92242454/191639700-573a936b-8e79-49e1-b64d-883467583edc.png">

 
