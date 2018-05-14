from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def list_products(request):
	products = Products.objects.all()
	return render(request, 'products.html', {'products': products})


@login_required
def create_product(request):
	if request.method == "POST":
		form = ProductForm(request.POST or None)

		if form.is_valid():
			form.save()
			return redirect('list_products')
	else:
		form = ProductForm()
		return render(request, 'products_add.html', {'form': form})


@login_required
def update_product(request, id):
	product = Products.objects.get(id=id)

	if request.method == "POST":
		form = ProductForm(request.POST or None, instance=product)
		if form.is_valid():
			form.save()
			return redirect('list_products')
	else:
		form = ProductForm(instance=product)
		return render(request, 'products_edit.html', {'form': form, 'product': product})


@login_required
def delete_product(request, id):
	product = Products.objects.get(id=id)

	if request.method == "POST":
		product.delete()
		return redirect('list_products')

	return render(request, 'delete-confirm.html', {'product': product})
