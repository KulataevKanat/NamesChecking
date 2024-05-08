from django.urls import path

from api.views import NamesWomanViews

urlpatterns = [
    path("create_names_woman/", NamesWomanViews.CreateNamesWomanView.as_view()),
    path("delete_names_woman_by_id/<int:pk>/", NamesWomanViews.DeleteNamesWomanByIdView.as_view()),
    path("find_all_names_woman/", NamesWomanViews.GetNamesWomanView.as_view()),
]
