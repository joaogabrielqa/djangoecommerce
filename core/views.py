from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    texts = ['Lorem ipsum dolor sit amet', 'Teste após alterações no Django!!!!']
    context = {
        'title': 'django e-commerce', 
        'texts': texts
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def product_list(request):
    return render(request, 'product_list.html')
