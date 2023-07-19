"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from my_work.views import start_page, work_page, UserListView, UserDetailView, UserCreateView, UserUpdateView, \
    UserDeleteView, SettingsListView, SettingsCreateView, SettingsDetailView, SettingsUpdateView, SettingsDeleteView, \
    MessageListView, MessageCreateView, MessageDetailView, MessageDeleteView, start_mailing, LogListView, \
    MessageUpdateView

app_name = 'my_work'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('start/', work_page, name='work_page'),
    path('clients/', UserListView.as_view(), name='clients'),
    path('clients/<int:pk>/', UserDetailView.as_view(), name='client'),
    path('clients/new/', UserCreateView.as_view(), name='user_create'),
    path('clients/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('clients/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('settings/', SettingsListView.as_view(), name='setting_list'),
    path('settings/new/', SettingsCreateView.as_view(), name='setting_create'),
    path('settings/<int:pk>/', SettingsDetailView.as_view(), name='setting_detail'),
    path('settings/update/<int:pk>/', SettingsUpdateView.as_view(), name='setting_update'),
    path('settings/delete/<int:pk>/', SettingsDeleteView.as_view(), name='setting_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('settings/startmailing/<int:pk>/', start_mailing, name='start_mailing'),
    path('settings/logs/', LogListView.as_view(), name='log'),
]
