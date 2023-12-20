from django import forms
from .models import CliantMessage


class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder":"Enter your name", "class":"form-control"}))
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.Textarea()
    class Meta:
        model = CliantMessage
        fields = ('__all__')