from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main_app.forms import NewNoteForm
from main_app.models import Note


class ListNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'main_app/note_index.html'

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by('-datetime')


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NewNoteForm

    template_name = 'main_app/new_note.html'

    def get_success_url(self):
        return reverse('main_app:list_notes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NewNoteForm

    template_name = 'main_app/update_note.html'

    def get_success_url(self):
        return reverse('main_app:list_notes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "main_app/delete_note.html"

    def get_success_url(self):
        return reverse('main_app:list_notes')
