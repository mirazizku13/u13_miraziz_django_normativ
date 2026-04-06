from django.shortcuts import render

from books.models import Books


def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/list.html', {"books":books})

def book_detail(request,pk):
    book = Books.objects.filter(id=pk).first()
    return render(request, 'books/detail.html', {"book":book})

def book_delete(request,pk):
    return None


