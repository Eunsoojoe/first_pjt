from django.shortcuts import render
from faker import Faker
import random

# Create your views here.
def index(request):    # 항상 인자에 request가 들어가는 것은 django의 규칙
    return render(request, 'index.html')

def root(request):
    return render(request, 'root.html')

def hello(request):
    username = 'eunsu'

    context = {
        'username' : username,

    } 

    return render(request, 'hello.html', context)

def lunch(request):
    menus = ['김밥','라면','떡볶이','쌀국수','돈까스']

    pick = random.choice(menus)
    #random.choice : iteration 객체의 요소 중 하나를 랜덤으로 추출

    context = {
        'pick':pick,
    }
    
    return render(request, 'lunch.html', context)

def lotto(request):
    lotto_num = random.sample(range(1,46),6)

    context = {
        'lotto_num':lotto_num,
    }

    return render(request, 'lotto.html', context)

def username(request, name):
    context = {
        'name': name,
    }

    return render(request, 'username.html', context)

def cube(request, number):
    result = number ** 3
    # 1. 위 코드에서 int()를 이용해 형변환을 하는 방법
    # 2. url.py내에서 path('cube/<int:number>/',views.cube)로 수정

    context = {
        'result' : result,
    } 

    return render(request, 'cube.html', context)

def posts(request):
    fake = Faker()
    fake_posts = []

    for i in range(100):
        fake_posts.append(fake.text())

    context = {
        'fake_posts' : fake_posts,
    }

    return render(request, 'posts.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # GET : ping에서 받아온 사용자의 데이터를 dict형태로 반환
    # request.GET.get('title')
    # info.get('name')
    title = request.GET.get('title')
    content = request.GET.get('content')

    context = {
        'title':title,
        'content':content,
    }

    return render(request,'pong.html',context)