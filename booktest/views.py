# coding=utf-8
from django.shortcuts import render
from django.db.models import Max, F, Q
from booktest.models import *
from django.http.response import HttpResponse
from django.shortcuts import redirect

def index(request):
    # contentList = BookInfo.book1.filter(heroinfo__hcontent__contains='八')
    contentList = BookInfo.book1.aggregate(Max('bpub_date'))
    gtList = BookInfo.book1.filter(bread__gt=F('bcommet'))
    QList = BookInfo.book1.filter(Q(pk__gt=5) | Q(bread=11))
    content = {'contentList': contentList, 'gtList': gtList, 'QList': QList}
    print(content.values())
    return render(request, 'booktest/index.html', content)


def getTest1(request):
    return render(request, 'booktest/getTest1.html')


def getTest2(request):
    a = request.GET['a1']
    b = request.GET['b1']
    content = {'a': a, 'b': b}
    return render(request, 'booktest/getTest2.html', content)


def getTest3(request):
    a = request.GET.getlist("a1")
    b = request.GET['b1']
    content = {'a': a, 'b': b}
    return render(request, 'booktest/getTest3.html', content)


def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    return render(request, 'booktest/postTest2.html')

def redTest(request):
    return redirect('/index/')

def returnTest(request,p):
    content={'p':p}
    return render(request, 'booktest/returnTest.html',content)