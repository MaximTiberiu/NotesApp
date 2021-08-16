from django import forms

from main_app.models import Note


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['author']


class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['author']
