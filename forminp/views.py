from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DonorForm
from django.contrib import messages
from .models import Donor

# Create your views here.
def index(request):
    return render(request, "forminp/home.html", {"donors": Donor.objects.all()})

def register(request):
    form = DonorForm()
    if request.method == 'POST':
        print(request.POST)
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.info(request, 'Donor already registered')

    context = {'form': form}
    return render(request, "forminp/register.html", context)

