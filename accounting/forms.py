from .models import AllIncome, AllExpenses, MonthlyIncome, MonthlyExpenses
from django import forms


class MonthlyIncomeForms(forms.ModelForm):
    class Meta:
        model = MonthlyIncome
        fields = '__all__'

class MonthlyExpensesForms(forms.ModelForm):
    class Meta:
        model = MonthlyExpenses
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'class':                 'form-control'}),
                   'summ': forms.NumberInput(attrs={'class': 'form-control'}),
                   'adress': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
                   'data': forms.SplitDateTimeWidget()
        }

class AllIncomeForms(forms.ModelForm):
    class Meta:
        model = AllIncome
        fields = '__all__'


class AllExpensesForms(forms.ModelForm):
    class Meta:
        model = AllExpenses
        fields = '__all__'