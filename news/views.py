from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.


def index(request):
    news = News.objects.order_by('-created_at')

    categories = Category.objects.all()

    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }

    return render(request, 'news/index.html', context)

    # print(dir(request))
    # print(request.META)
    # news = News.objects.all()
    # res = '<H1>Список новостей</H1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)
    # return HttpResponse('hello world!')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }

    return render(request, 'news/category.html', context)

