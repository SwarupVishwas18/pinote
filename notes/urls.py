from unicodedata import name
from django.urls import path
from . import views
import django.contrib.auth.views as views_aut

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views_aut.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('deletenote/<note_id>', views.delete_record, name='deletenote'),
    path('downloadnote/<note_id>', views.download_note, name='downloadnote'),
    path('copynote/<note_id>', views.copy_note, name='copynote')
]
