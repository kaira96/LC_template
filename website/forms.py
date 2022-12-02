from django import forms
from .models import Lead
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        # fields = '__all__'
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : '0700123456'}),
        }

    # def clean_title(self):
    #     title = self.cleaned_data['phone_number']
    #     if re.match(r'\d{10}', title):
    #         raise ValidationError('Название должно содержать номер телефона в формате 0700123456')
    #     return title