from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    database_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': database_katalog,
        'Nama': 'Dina Dwi Kinanty 🌸',
        'NPM': '2106751650'
    }
    return render(request, "katalog.html", context)