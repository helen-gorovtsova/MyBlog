from django import forms
from todo.models import TodoList, Category


class ToDoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
            'title': forms.TextInput(),
            'deadline': forms.DateTimeInput(),
            'status': forms.HiddenInput(),
            'category': forms.SelectMultiple(),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
        }