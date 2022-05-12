# accountapp/views.py
from django.shortcuts import render
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()# 모델의 클래스로 인스턴스 생성
        new_hello_world.text = temp# 인스턴스 메소드에 temp로 받은 데이터를 넣음| temp는 위에서 post로 template에서 input name으로 전달받은 데이터
        new_hello_world.text_model_test = temp
        new_hello_world.save() # db에 저장

        return render(request, 'accountapp/hello_world.html',context={'hello_world_output': new_hello_world})#객체를 내보냄
    else:
        return render(request, 'accountapp/hello_world.html',context={'text': 'GET METHOD'})