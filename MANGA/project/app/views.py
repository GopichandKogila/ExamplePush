from django.shortcuts import render, redirect
from .models import Author,Book



def home(request):
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})

def createAuthor(request):
    if request.method == 'POST':
        name = request.POST.get('aname')
        age = request.POST.get('age')
        rating = request.POST.get('rate')
        author = Author(name=name, age=age, rating=rating)
        author.save()
    return render(request, 'author.html')

def createBook(request):
        if request.method == 'POST':
            title = request.POST.get('bname')
            price = request.POST.get('price')
            genre = request.POST.get('genre')
            authorid = request.POST.get('sno')
            image = request.FILES.get('img')
            caption = request.FILES.get('cap')
            if Author.objects.filter(id=authorid).exists():
                a=Author.objects.get(id=authorid)
                book = Book(title=title, price=price, genre=genre, author=a)
                book.save()
                return redirect('home')

        return render(request, 'book.html')
