from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from my_work.form import UserCreateForm
from my_work.models import Client


def start_page(request):
    context = {
        'title': 'Стартовая',
    }
    return render(request, 'index.html', context=context)


def work_page(requests):
    return render(requests, 'work_page.html')


def t_view(requests):
    return render(requests, 't_view.html')


class UserListView(generic.ListView):
    model = Client
    template_name = 'user/user_list.html'


class UserDetailView(generic.DetailView):
    model = Client
    template_name = 'user/user_detail.html'


class UserCreateView(generic.CreateView):
    model = Client
    template_name = 'user/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('my_work:clients')


class UserUpdateView(generic.UpdateView):
    model = Client
    template_name = 'user/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('my_work:clients')


class UserDeleteView(generic.DeleteView):
    model = Client
    template_name = 'user/user_detail.html'
    success_url = reverse_lazy('my_work:clients')
