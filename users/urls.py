from django.urls import path

from .views import login_page, logout_page

urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
