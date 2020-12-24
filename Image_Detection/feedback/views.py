from django.shortcuts import render
from .models import feedback
from .forms import feedbackform
# Create your views here.
def feedback_create(request):
        form=feedbackform(request.POST or None)
        if form.is_valid():
                form.save()
        context={
                'form':form
                }
        return render(request, "feedback/feedback.html", context)
