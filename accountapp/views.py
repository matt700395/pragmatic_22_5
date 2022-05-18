# accountapp/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()# 모델의 클래스로 인스턴스 생성
            new_hello_world.text = temp# 인스턴스 메소드에 temp로 받은 데이터를 넣음| temp는 위에서 post로 template에서 input name으로 전달받은 데이터
            new_hello_world.save() # db에 저장

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'

    def get(self, *args, **kwargs):
        if self.request.user.is_autenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_autenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()


class AccountDeleteView(DeleteView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'

    def get(self, *args, **kwargs):
        if self.request.user.is_autenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_autenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
