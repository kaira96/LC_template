from django.contrib import admin
from .models import MonthlyIncome, MonthlyExpenses

class MonthlyIncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summ', 'data', 'adress')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summ', 'data')
    list_filter = ('data',)
    fields = ('title', 'summ', 'adress', 'data')
    save_on_top = True


class MonthlyExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summ', 'data', 'adress')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summ', 'data')
    list_filter = ('data',)
    fields = ('title', 'summ', 'adress', 'data')
    save_on_top = True



admin.site.register(MonthlyIncome, MonthlyIncomeAdmin)
admin.site.register(MonthlyExpenses, MonthlyExpensesAdmin)
