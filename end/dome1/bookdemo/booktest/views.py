from django.shortcuts import render, redirect, reverse

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
    return render(request, 'index.html', {'books': books})


def about(request):
    return HttpResponse("这里是应用的关于页")


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    return redirect(to='/')


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)


def addhero(request, bookid):
    if request.method == 'GET':
        return render(request, 'addhero.html')
    elif request.method == 'POST':
        hero = Hero()
        hero.name = request.POST.get('heroname')
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("herogender")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)


def addbook(request):
    if request.method == "GET":
        return render(request, 'addbook.html')
    elif request.method == "POST":
        book = Book()
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.bpub_date = request.POST.get('pub_date')
        book.save()

        url = reverse("booktest:index")
        return redirect(to=url)


def editbook(request, bookid):
    book = Book.objects.get(id=bookid)
    print(book.bpub_date)
    if request.method == "GET":
        return render(request, "editbook.html", {"book": book})
    elif request.method == "POST":
        book.title = request.POST.get("title")
        book.price = request.POST.get("price")
        book.bpub_date = request.POST.get("pub_date")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)


def edithero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == "GET":
        return render(request, "edithero.html", {"hero": hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("herogender")
        hero.content = request.POST.get("herocontent")
        hero.save()
        bookid = hero.book.id
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)
