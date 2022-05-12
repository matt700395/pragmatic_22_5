from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        # 모델의 클래스로 인스턴스 생성
        new_hello_world = HelloWorld()

        # 인스턴스 메소드에 temp로 받은 데이터를 넣음| temp는 위에서 post로 template에서 input name으로 전달받은 데이터
        new_hello_world.text = temp

        # db에 저장
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_output': new_hello_world})#객체를 내보냄
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})
    #return render(request, 'base.html')
    #return HttpResponse('Hello World!')