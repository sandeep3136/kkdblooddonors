from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DonorForm
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

    context = {'form': form}
    return render(request, "forminp/register.html", context)

