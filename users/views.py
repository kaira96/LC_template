from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from .models import Product, Supplier, Buyer, Order


# @login_required(login_url='login')
# def dashboard(request):
#     total_product = Product.objects.count()
#     total_supplier = Supplier.objects.count()
#     total_buyer = Buyer.objects.count()
#     total_oder = Order.objects.count()
#     orders = Order.objects.all().order_by('-id')
#     context = {
#         'product': total_product,
#         'supplier': total_supplier,
#         'buyer': total_buyer,
#         'order': total_oder,
#         'orders': orders
#     }
#     return render(request, 'dashboard.html', context)



def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')
