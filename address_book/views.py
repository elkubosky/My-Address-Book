from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

def home(request):
	all_addresses = Address.objects.all
	return render(request, 'home.html', {'all_addresses': all_addresses})

def add_address(request):
	if request.method == 'POST': # if someone click on the button, they POST the data, and do what above
		form = AddressForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Address Has Been Added!"))
			return redirect('home')
		else:
			messages.success(request, ('Seems like there was an error...'))
			return render(request, 'add_address.html', {})
	else: 
		return render(request, 'add_address.html', {}) # otherwise just re-show the form


def edit(request, list_id):
	if request.method == 'POST': 
		current_address = Address.objects.get(pk=list_id) # we don`t want all objects, only one we want to edit
		form = AddressForm(request.POST or None, instance=current_address)
		if form.is_valid():
			form.save()
			messages.success(request, ("Address Has Been Edited!"))
			return redirect('home')
		else:
			messages.success(request, ('Seems like there was an error...'))
			return render(request, 'edit.html', {})
	else: 
		get_address = Address.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_address': get_address}) # otherwise just re-show the form


def delete(request, list_id):
	if request.method == 'POST': 
		current_address = Address.objects.get(pk=list_id) 
		current_address.delete()
		messages.success(request, ("Address Has Been Deleted"))
		return redirect('home')
	else:
		messages.success(request, ('Nothing To See Here...'))
		return render(request, 'home', {})


