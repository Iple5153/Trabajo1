from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):

	return render(request, 'registration/home.html')

def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		    form.save()
		    return redirect('/account/login')
		else:
			form = UserCreationForm()

			args = {'form': form}
			return render(request, 'registration/reg_form.html', args)
	else:
			form = UserCreationForm()

			args = {'form': form}
			return render(request, 'registration/reg_form.html', args)