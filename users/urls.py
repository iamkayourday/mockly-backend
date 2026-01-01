from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView, RandomUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:id>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:id>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/random/', RandomUserView.as_view(), name='random-user'),
]