from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.views.generic import (
	DetailView,
	UpdateView,
	DeleteView
)

from django.urls import reverse_lazy

# Create your views here.
class ProductUpdateView(UpdateView):
	template_name = 'product/product_create.html'
	form_class = ProductForm
	queryset = Product.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)


class ProductDetailView(DetailView):
	template_name = 'product/product_detail.html'
	queryset = Product.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, 'product/product_create.html', context)


def home_view(request):
	queryset = Product.objects.all()
	print(queryset)
	context = {
		'object_list': queryset
	}
	return render(request, 'home.html', context)

class ProductDeleteView(DeleteView):
	template_name = 'product/product_delete.html'
	queryset = Product.objects.all()
	success_url = '/'
	# reverse_lazy('home-view')

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)

