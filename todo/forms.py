from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='What needs to be done?', max_length=255)

class NoteForm(forms.Form):
    text = forms.CharField(label='Add note:', max_length=255)