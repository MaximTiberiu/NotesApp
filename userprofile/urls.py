from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('update_profile/<int:pk>', views.UpdateProfileView.as_view(), name='update_account'),
    path('new_account/', views.CreateNewUser.as_view(), name='add_new_account'),
]