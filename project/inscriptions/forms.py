from django import forms
from .models import index

class indexForm(forms.ModelForm):
    class Meta:
        model = index
        fields = ['nom', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
