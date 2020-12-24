from django import forms
from .models import crime
class crimeform(forms.ModelForm):
        class Meta:
                model=crime
                fields=[
                        'name',
                        'gender',
                        'age',
                        'height',
                        'location',
                        'crime',
                        'photo'
                        ]
