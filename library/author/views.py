from django.shortcuts import render, redirect
from .models import Author

def author_list(request):
    authors = Author.get_all() 
    return render(request, 'author/author_list.html', {'authors': authors})

def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        if name and surname and patronymic:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return redirect('author_list')

    return render(request, 'author/create_author.html')