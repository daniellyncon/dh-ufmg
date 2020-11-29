# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# from .models import User
#
#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('email',)
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('email',)

from django import forms
import datetime


class MyDateWidget(forms.TextInput):

    def render(self, name, value, attrs=None, **kwargs):
        if isinstance(value, datetime.date):
            value = value.strftime("%d/%m/%Y")

        return super(MyDateWidget, self).render(name, value, attrs)


class MyDateField(forms.DateField):
    widget = MyDateWidget
    needs_multipart_form = True
    is_hidden = False

    def __init__(self, *args, **kwargs):
        super(MyDateField, self).__init__(*args, **kwargs)
        self.input_formats = ("%d/%m/%Y",)
