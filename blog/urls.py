from django.urls import path
from .views import ItemsListView, ItemsDetailView, items_detail, ItemsCreateView, ItemsDeleteView, ItemsUpdateView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', ItemsListView.as_view(), name="home"),
    path('<uuid:pk>', items_detail, name='items_detail'),
    path('<uuid:pk>/update/', ItemsUpdateView.as_view(), name='items_update'),
    path('<uuid:pk>/delete/', ItemsDeleteView.as_view(), name='items_delete'),
    path('<uuid:pk>/create/', ItemsCreateView.as_view(), name='items_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
