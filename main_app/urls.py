from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.ListNotesView.as_view(), name='list_notes'),
    path('new_note/', views.CreateNoteView.as_view(), name='add_new_note'),
    path('edit_note/<int:pk>', views.UpdateNoteView.as_view(), name='update_note'),
    path('delete_note/<int:pk>', views.DeleteNoteView.as_view(), name='delete_note')
]