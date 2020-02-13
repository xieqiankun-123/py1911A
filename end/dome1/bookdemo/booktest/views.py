from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Book, Hero


def index(request):
    # template = loader.get_template('index.html')
    books = Book.objects.all()
    # context = {'books': books}
    #
    # result = template.render(context)
    #
    # return HttpResponse(result)
    return render(request,'index.html',{'books':books})


def about(request):
    return HttpResponse("这里是应用的关于页")


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})
