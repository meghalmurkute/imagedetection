from django import forms
from .models import news
class newsform(forms.ModelForm):
        class Meta:
                model=news
                fields=[
                        'title',
                        'news'
                        ]
