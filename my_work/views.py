from django.shortcuts import render
from django.views.generic import ListView

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


class UserListView(ListView):
    model = Client
    template_name = 'user/user_list.html'
