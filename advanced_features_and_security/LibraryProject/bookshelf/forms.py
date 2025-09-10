# bookshelf/forms.py
from django import forms
from .models import Book  # if you're using a model form

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

#if it's a ModelForm
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
