from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='epay-Home'),
    path('signup/', views.signup, name='epay-signup'),
    path('item/<int:pk>/', PostDetailView.as_view(), name='item-detail'),
    path('item/new/', PostCreateView.as_view(), name='item-create'),
    path('search/', views.searchView, name='searchview'),
    path('search1/', views.searchView1, name='searchview1'),
    path('item/<int:pk>/update/', PostUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', PostDeleteView.as_view(), name='item-delete'),
    path('bid/', views.bidView, name='bidView'),

]
