from django.shortcuts import render, redirect
from .models import Author

def author_list(request):
    authors = Author.get_all() 

    return render(request, 'author/author_list.html', {'authors': authors})