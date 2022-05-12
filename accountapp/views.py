# accountapp/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()# 모델의 클래스로 인스턴스 생성
        new_hello_world.text = temp# 인스턴스 메소드에 temp로 받은 데이터를 넣음| temp는 위에서 post로 template에서 input name으로 전달받은 데이터
        new_hello_world.save() # db에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})