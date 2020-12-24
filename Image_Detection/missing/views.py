from django.shortcuts import render
from .models import miss
from .forms import missform
# Create your views here.
def miss_create(request):
        form=missform(request.POST or None)
        if form.is_valid():
                form.save()
        context={
                'form':form
                }
        return render(request, "miss/miss.html", context)
