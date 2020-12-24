from django.shortcuts import render
from .models import crime
from .forms import crimeform
# Create your views here.
def crime_create(request):
        form=crimeform(request.POST or None)
        if form.is_valid():
                form.save()
        context={
                'form':form
                }
        return render(request, "crime/crime.html", context)
