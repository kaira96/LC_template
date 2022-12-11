from django import forms
from .models import Student
from accounting.models import MonthlyIncome, MonthlyExpenses, AllIncome, AllExpenses


class StudentForm(forms.ModelForm):
 class Meta:
     model = Student
     fields = '__all__'
     widgets = {
         'name': forms.TextInput(attrs={'class': 'form-control'}),
         'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
         'course': forms.Select(attrs={'class': 'form-control'}),
         'tariff': forms.Select(attrs={'class': 'form-control'}),
         'payment': forms.NumberInput(attrs={'class': 'form-control'}),
         'data': forms.SelectDateWidget(attrs={'class': 'form-control'}),
         'finished': forms.SelectDateWidget(attrs={'class': 'form-control'}),
         'certificate': forms.FileInput(attrs={'class': 'form-control'}),
         'accept': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
     }