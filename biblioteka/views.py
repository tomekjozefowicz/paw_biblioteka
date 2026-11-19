from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Biblioteka</h1>"
        "<p>Aplikacja Django działa poprawnie.</p>"
        '<p><a href="/books/">Przejdź do książek</a></p>'
    )


def book_list(request):
    return HttpResponse(
        "<h1>Lista książek</h1>"
        "<ul>"
        "<li>Solaris — Stanisław Lem</li>"
        "<li>Lalka — Bolesław Prus</li>"
        "<li>Hobbit — J.R.R. Tolkien</li>"
        "</ul>"
        '<p><a href="/">Powrót</a></p>'
    )