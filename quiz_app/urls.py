from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),  # Home page
    path('signup/', views.signup_view, name='signup'),  # Signup view
    path('create/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/add-question/', views.add_question, name='add_question'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('submit/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
    path('quiz-summary/', views.quiz_summary, name='quiz_summary'),
    path('quiz/<int:quiz_id>/result/', views.view_result_detail, name='view_result_detail'),
]