from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Key,keyHistory


def index(request):
    #return HttpResponse("<h1>this is the keystate page </h1>")
    all_keys = Key.objects.all()

    context = { 'all_keys': all_keys  }
    return render(request,'keystate/index.html',context)

def detail(request,Key_id):
    #return HttpResponse("<h2> Details for the key id: " + str(Key_id) + "</h2>")
    try:
        thekey = Key.objects.get(pk=Key_id)

    except Key.DoesNotExist:
        raise Http404("Key does not exist")
    return render(request, 'keystate/detail.html', {'thekey': thekey  })