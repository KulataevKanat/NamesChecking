from django.urls import path

from api.views import ContactViews

urlpatterns = [
    path('update_gender/', ContactViews.UpdateContacts.as_view()),
    path('find_all/', ContactViews.GetContactsView.as_view()),
]
