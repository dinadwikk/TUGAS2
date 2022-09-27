from django.shortcuts import render
from mywatchlist.models import ContentMyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
# def show_html(request):
#     #return render(request, "wishlist.html")
#     data_film = ContentMyWatchList.objects.all()
#     context = {
#     'data_film': data_film,
#     'nama': 'Dina 🌈',
#     'id' : '2106751650'
#     }
#     return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = ContentMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = ContentMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

