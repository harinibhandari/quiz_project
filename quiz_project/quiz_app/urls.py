from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login URL
    path('subjects/', views.subject_list, name='subjects'),  # Subject list URL
    path('quiz/<int:subject_id>/', views.quiz_view, name='quiz'),  # Quiz URL
]
