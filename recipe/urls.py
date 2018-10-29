from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('vote/', views.vote, name='vote'),
]
