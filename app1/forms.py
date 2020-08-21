from .models import ToDo
from django import forms

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'important']
        # widgets = {
        # 'time_completed': DateInput()
        # }
