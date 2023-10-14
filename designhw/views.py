from django.shortcuts import render
from django.http import HttpResponse
from designhw.models import News

def main(request):
    news = News.objects.all()
    context={
        'news':news
    }
    return render(request,'designhw/news.html',context=context)