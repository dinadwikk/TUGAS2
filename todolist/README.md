# TUGAS 4

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

Heroku app url : https://dinaherokuver.herokuapp.com/todolist/

Nama  : Dina Dwi K.
NPM   : 2106751650
PBP   : PBP-B

# Pendahuluan
Pada tugas ini, kamu akan mengimplementasikan elemen `<form>`, konsep autentikasi, dan beberapa hal yang sudah kita pelajari selama tutorial lab. Form adalah bagian dari HTML yang dapat digunakan untuk membuat elemen formulir pada halaman web. 
Passing argumet method :
POST:
- Menambahkan formulir-data di dalam isi permintaan HTTP (data tidak ditampilkan dalam URL)
- Pengiriman formulir dengan POST tidak dapat di-bookmark

GET:
- Jangan pernah menggunakan GET untuk mengirim data sensitif! (akan terlihat di URL)
- Berguna untuk pengiriman formulir di mana pengguna ingin menandai hasil
- GET lebih baik untuk data yang tidak aman, seperti string kueri di Google

# `{% csrf_token %}` pada elemen `<form>`

`{% csrf_token %}` berguna untuk melakukan verifikasi user dan site. `{% csrf_token %}` akan menghasilkan token yang dibuat oleh server dan dikirim melalui HTTP Reqiest. 
Jika developer tidak menggunakan `{% csrf_token}` pada `<form>` maka hal tersebut dapat mempermudah hacker untuk melakukan serangan pada website.

#  `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }}

Selain menggunakan form generator, kita dapat membuat form secara manual. Tentu hal tersebut akan terkesan lebih ribet dibandingkan dengan menggunakan form. 
Namun jika diggambarkan, maka beginilah bentuk form manual :
```
<form action="http://www.sesuatu.com/proses"
method="POST">
    Name: <input type="text">
    <input type="submit" value="Submit">
</form>
```

# Proses Alur Data `<form>` pada HTML
Berikut penjelasan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML :

User akan memberikan input pada form, input inilah yang akan di response oleh browser dan mengirimkannya pada POST request ke dalam server. Data akan diolah lalu disimpan pada database server. 
Data tersebut akan disalurkan dan diresponse oleh Djanggo `views.py` lalu data yang didapat akan kelola dan disimpan. Data yang telah diproses akan muncul di page HTML setelah melakukan pembaharuan page.

# Impementasi
1. Buat suatu aplikasi baru bernama `todolist` di proyek Django Tugas 2 pekan lalu
2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah kamu buat ke dalam proyek Django-mu. Contohnya adalah sebagai berikut. 
  ```
  INSTALLED_APPS = [
    ...,
    'todolist',
]
```
3. Buka file `models.py` yang ada di folder `todolist` dan tambahkan potongan kode berikut.
```
class TodolistTemplate(models.Model):
    id = models.AutoField (primary_key= True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank= True, null= True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
```
4. Lakukan perintah `python manage.py makemigrations' lalu lakukan python `manage.py migrate` untuk mempersiapkan migrasi dan menerapkan skema model ke dalam database Django lokal.
5. Buatlah fungsi fungsi yang dibutuhkan pada progam `todolist` pada `views.py`
```
login_required(login_url='/todolist/login/')
def show_todolist(request):
    ...

def register(request):
    ...

def login_user(request):
    ...

def logout_user(request):
    ...

@login_required(login_url='/todolist/login/')
def create(request):
   ...
```
6. Buat folder `templates` di dalam folder `todolist` lalu tambahkan kode html
- Create.html
- Login.html
- Register.html
- Todolist.html
7. Daftarkan  aplikasi `todolist` dalam `urls.py` yang ada pada folder `project_django`
8. Jalankan aplikasi dengan `python manage.py runserver` lalu buka `http://localhost:8000/mywatchlist/` aplikasi siap digunakan

# SOURCE
  https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1
  https://scele.cs.ui.ac.id/pluginfile.php/161881/mod_resource/content/1/05%20-%20Form%2C%20Authentication%2C%20Session%2C%20and%20Cookie.pdf
  https://socs.binus.ac.id/2018/12/05/form-pada-html/

