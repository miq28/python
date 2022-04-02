
# Create your views here.

from django.shortcuts import HttpResponse, render


def index(req):
    # context harus dict aka JSON
    context = {
        'title': 'Dapur',
        'content': ['home', 'about', 'contact']
    }
    return render(req, 'home.html', context=context)

def contact(req):
    return render(req, 'contact.html')

