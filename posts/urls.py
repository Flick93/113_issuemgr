from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="published"),
    path("drafts/", views.DraftPostListView.as_view(), name="draft"),
    path("archived/", views.ArchivedPostListView.as_view(), name="archived"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("new/", views.PostCreateView.as_view(), name="new"),
]