from django import forms
from .models import feedback
class feedbackform(forms.ModelForm):
        class Meta:
                model=feedback
                fields=[
                        'name',
                        'email_id',
                        'issue'
                        ]
