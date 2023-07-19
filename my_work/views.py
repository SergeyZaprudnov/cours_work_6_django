from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now

from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView

from my_work.form import UserCreateForm, SettingCreateForm, MessageCreateForm
from my_work.models import Client, Setting, Messages, Logs
from my_work.utils.utils import AutoMail


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


class UserDetailView(DetailView):
    model = Client
    template_name = 'user/user_detail.html'


class UserCreateView(CreateView):
    model = Client
    template_name = 'user/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('my_work:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = Client
    template_name = 'user/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('my_work:clients')


class UserDeleteView(DeleteView):
    model = Client
    template_name = 'user/user_detail.html'
    success_url = reverse_lazy('my_work:user_list')


class SettingsListView(ListView):
    model = Setting
    template_name = 'settings/setting_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['data'] = {
            'status': 'Статус',
        }
        return context


class SettingsDetailView(DetailView):
    model = Setting
    template_name = 'settings/setting_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = {
            'status': 'Статус',
            'start': 'Дата начала рассылки',
            'end': 'Дата окончания рассылки',
            'periodicity': 'Периодичность'
        }
        return context


class SettingsCreateView(CreateView):
    model = Setting
    template_name = 'settings/setting_create.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('my_work:setting_list')


class SettingsUpdateView(UpdateView):
    model = Setting
    template_name = 'settings/setting_create.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('my_work:setting_list')


class SettingsDeleteView(DeleteView):
    model = Setting
    template_name = 'settings/setting_delete.html'
    success_url = reverse_lazy('my_work:setting_list')


class MessageListView(ListView):
    model = Messages
    template_name = 'message/message_list.html'


class MessageDetailView(DetailView):
    model = Messages
    template_name = 'message/message_detail.html'


class MessageCreateView(CreateView):
    model = Messages
    template_name = 'message/message_create.html'
    success_url = reverse_lazy('my_work:message_list')
    form_class = MessageCreateForm


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Messages
    template_name = 'message/message_create.html'
    success_url = reverse_lazy('my_work:message_list')
    form_class = MessageCreateForm


class MessageDeleteView(DeleteView):
    model = Messages
    template_name = 'message/message_delete.html'
    success_url = reverse_lazy('my_work:message_list')


def start_mailing(request, pk):
    context = {'result': 'Рассылка запущена'}

    data = Setting.objects.get(id=pk)
    Logs.objects.create(
        title=f'Запуск: {data.mailing_name}',
        date_last=now(),
        status='Рассылка включена',
        answer='Без ответа',
        settings=data,
    )

    a = AutoMail(data)
    return render(request, 'my_work/a_mail.html', context=context)


class LogListView(ListView):
    model = Logs
    template_name = 'log.html'
