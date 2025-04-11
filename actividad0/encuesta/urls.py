from django.urls import path

from . import views

app_name = "encuesta"
urlpatterns = [
    # ex: /encuesta/
    path("", views.index, name="index"),
    # ex: /encuesta/5/
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
