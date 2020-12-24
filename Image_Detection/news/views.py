from django.shortcuts import render, redirect
from .models import news
from .forms import newsform
# Create your views here.

def news_detail_view(request):
        queryset = news.objects.all()
        context={
                'obj':queryset
                 }
        return render(request, "news/news.html",context)
