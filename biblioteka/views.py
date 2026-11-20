from django.shortcuts import render

from .models import Author, Book


def home(request):
    context = {
        "books_count": Book.objects.count(),
        "authors_count": Author.objects.count(),
    }

    return render(
        request,
        "biblioteka/home.html",
        context,
    )


def book_list(request):
    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(
        request,
        "biblioteka/book_list.html",
        context,
    )


def author_list(request):
    authors = Author.objects.all()

    context = {
        "authors": authors,
    }

    return render(
        request,
        "biblioteka/author_list.html",
        context,
    )


def contact(request):
    return render(
        request,
        "biblioteka/contact.html",
    )


def about(request):
    return render(
        request,
        "biblioteka/about.html",
    )