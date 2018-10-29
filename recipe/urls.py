from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
	path('<int:pk>/delete/', views.delete, name='delete'),
	path('<int:pk>/send_to_cart/', views.send_to_cart, name='send_to_cart'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('vote/', views.vote, name='vote'),
]
