from django.shortcuts import render
from django.http import HttpResponse
from modelstest.models import Author,Blog

def main(request):
    blogs = Blog.objects.all().order_by('-content')

    return HttpResponse(f"{blogs[0].content} ; {blogs[1].content}")