from django import forms

from my_work.models import Client, Setting, Messages


class UserCreateForm(forms.ModelForm):
    name = forms.CharField(label='ФИО')
    email = forms.EmailField(label='email')
    comment = forms.CharField(label='Комментарий')

    class Meta:
        model = Client
        fields = ('name', 'email', 'comment')


class SettingCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget = forms.HiddenInput()

    class Meta:
        model = Setting
        fields = '__all__'


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
