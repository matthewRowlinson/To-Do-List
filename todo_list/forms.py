from django import forms
from .models import List

#creating a "ListForm" from django's models.List it has an item, our to-do list item such as take out garbage, or finish project, and completed, ...
#a Boolean that allows the program to know if an item is "completed" or not
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
