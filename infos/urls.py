from django.urls import path
from .views import show_main_page, show_about_me_page, show_contact_page

urlpatterns = [
   path('', show_main_page),
   path('me', show_about_me_page),
   path('contact', show_contact_page),
]