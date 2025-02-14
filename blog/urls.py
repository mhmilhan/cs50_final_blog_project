from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>/add_post/', views.add_post_view, name='add_post_view'),
    path('<str:category>/', views.post_by_category, name='post_by_category'),
    path('success_post_submission/', views.success_view, name='success_view'),
    path('<str:category>/<uuid:post_id>/', views.post_detail, name='post_detail'),
]


