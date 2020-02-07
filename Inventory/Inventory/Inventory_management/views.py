# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def home(request):
	return render(request, 'inventory/index.html');


# Display devices

def display_desktops(request):
	items = Desktop.objects.all()
	context = {
		'items': items,
		'header': 'Desktops'
	}

	return render(request, 'inventory/index.html', context)

def display_laptops(request):
	items = Laptop.objects.all()
	context = {
		'items': items,
		'header': 'Laptops'
	}

	return render(request, 'inventory/index.html', context)

def display_mobiles(request):
	items = Mobile.objects.all()
	context = {
		'items': items,
		'header': 'Mobiles'
	}

	return render(request, 'inventory/index.html', context)


# Add devices


def add_desktops(request):
	if request.method =="POST":
		form = DesktopForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('display_desktops')

	else:
		form = DesktopForm()
		return render(request, 'inventory/add_new.html', {'form': form})


def add_laptops(request):
	if request.method =="POST":
		form = LaptopForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('display_laptops')

	else:
		form = LaptopForm()
		return render(request, 'inventory/add_new.html', {'form': form})



def add_mobiles(request):
	if request.method =="POST":
		form = MobileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('display_mobiles')

	else:
		form = MobileForm()
		return render(request, 'inventory/add_new.html', {'form': form})

#Edit devices


def edit_desktop(request, pk):
	item = get_object_or_404(Desktop, pk=pk)

	if request.method == "POST":
		form = DesktopForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_desktops')

	else:
		form= DesktopForm(instance=item)
		return render(request, 'inventory/edit_item.html', {'form': form})

def edit_laptop(request, pk):
	item = get_object_or_404(Laptop, pk=pk)

	if request.method == "POST":
		form = LaptopForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_laptops')

	else:
		form= LaptopForm(instance=item)
		return render(request, 'inventory/edit_item.html', {'form': form})

def edit_mobiles(request, pk):
	item = get_object_or_404(Mobile, pk=pk)

	if request.method == "POST":
		form = MobileForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_mobiles')

	else:
		form= MobileForm(instance=item)
		return render(request, 'inventory/edit_item.html', {'form': form})



# Delete device

def delete_desktop(request, pk):
	Desktop.objects.filter(id=pk).delete()
	items = Desktop.objects.all()
	context = {
		'items': items,
	}
	return render(request, 'inventory/index.html', context)


def delete_laptop(request, pk):
	Laptop.objects.filter(id=pk).delete()
	items = Laptop.objects.all()
	context = {
		'items': items,
	}
	return render(request, 'inventory/index.html', context)


def delete_mobile(request, pk):
	Mobile.objects.filter(id=pk).delete()
	items = Mobile.objects.all()
	context = {
		'items': items,
	}
	return render(request, 'inventory/index.html', context)