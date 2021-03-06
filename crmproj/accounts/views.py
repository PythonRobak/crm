from django.shortcuts import render
from .models import *

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered_orders = orders.filter(status='Delivered').count()
	pending_orders = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers, 'total_customers':total_customers,
			   'total_orders':total_orders, 'delivered_orders':delivered_orders, 'pending_orders':pending_orders}

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

def customer(request):
	return render(request, 'accounts/customer.html')