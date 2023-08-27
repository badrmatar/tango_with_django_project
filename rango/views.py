from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse


def index(request):
    categories_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['categories'] = categories_list

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
