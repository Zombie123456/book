from django.shortcuts import render
from .models import *
# Create your views here.


def index_views(request):
    l = []
    for i in range(1,50):
        name = eval('S%s().table_name()' % i)
        url = eval('S%s().url()' % i)
        l.append((name,url))




    session = '小明'
    return render(request, 'index.html', locals())

def story_views(request):
    name = request.GET['name']
    s = '%s.objects.all()' % name
    obj = eval(s)
    return render(request, 'story.html', locals())

def chapter_views(request):
    name = request.GET['name']
    chapter = int(request.GET['chapter'])
    s = '%s.objects.all()' % name
    count = len(eval(s))
    s = '%s.objects.filter(id="%s")'%(name,chapter)
    obj = eval(s)
    chapter_name = obj[0].chapter
    obj = obj[0].comment.replace('&nbsp;','').split('。')
    return render(request, 'chapter.html', locals())