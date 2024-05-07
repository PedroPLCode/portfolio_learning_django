from django.urls import path
from .views import show_main_page, show_about_me, show_contact

urlpatterns = [
   path('', show_main_page),
   path('me', show_about_me),
   path('contact', show_contact),
]