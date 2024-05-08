from django.urls import path

from api.views import NamesManViews

urlpatterns = [
    path("create_names_man/", NamesManViews.CreateNamesManView.as_view()),
    path("delete_names_man_by_id/<int:pk>/", NamesManViews.DeleteNamesManByIdView.as_view()),
    path("find_all_names_man/", NamesManViews.GetNamesManView.as_view()),
]
