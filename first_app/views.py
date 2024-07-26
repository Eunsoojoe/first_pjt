from django.shortcuts import render
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