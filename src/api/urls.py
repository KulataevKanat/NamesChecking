from django.urls import path, include

from api.endpoints import NamesManEndpoints, NamesWomanEndpoints, ContactEndpoints

urlpatterns = [
    path('names_man/', include(NamesManEndpoints)),
    path('names_woman/', include(NamesWomanEndpoints)),
    path('contacts/', include(ContactEndpoints)),
]
