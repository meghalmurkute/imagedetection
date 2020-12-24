from django import forms
from .models import miss
class missform(forms.ModelForm):
        class Meta:
                model=miss
                fields=[
                        'name',
                        'gender',
                        'age',
                        'height',
                        'address',
                        'missing_location',
                        'contact_number',
                        'email_id',
                        'photo'
                        ]
