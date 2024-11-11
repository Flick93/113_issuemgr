from django.urls import path
from .views import (
    IssueListView,
    IssueDetailView,
    IssueUpdateView,
    IssueDeleteView,
    IssueCreateView,
)
urlpatterns = [
    path("", IssueListView.as_view(), name="list"),
    path("<int:pk>/", IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", IssueUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", IssueDeleteView.as_view(), name="delete"),
    path("new/", IssueCreateView.as_view(), name="new"),
]