from django.contrib import admin
from .models import MonthlyIncome, MonthlyExpenses, AllIncome, AllExpenses

class MonthlyIncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summ', 'data', 'adress', 'total')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summ', 'data')
    list_filter = ('data',)
    fields = ('title', 'summ', 'adress', 'data')
    save_on_top = True


class MonthlyExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summ', 'data', 'adress', 'total')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summ', 'data')
    list_filter = ('data',)
    fields = ('title', 'summ', 'adress', 'data')
    save_on_top = True

class AllIncodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'summ', 'data',)
    list_display_links = ('id', 'summ')
    search_fields = ('summ', 'data')
    list_filter = ('data',)
    fields = ('summ',)
    save_on_top = True

class AllExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'summ', 'data',)
    list_display_links = ('id', 'summ')
    search_fields = ('summ', 'data')
    list_filter = ('data',)
    fields = ('summ',)
    save_on_top = True


admin.site.register(AllExpenses, AllExpensesAdmin)
admin.site.register(AllIncome, AllIncodeAdmin)
admin.site.register(MonthlyIncome, MonthlyIncomeAdmin)
admin.site.register(MonthlyExpenses, MonthlyExpensesAdmin)
