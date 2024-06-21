from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('completed/', views.completed, name='completed'),
    path('edit/', views.edit, name='edit'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('profile/', views.profile, name='profile'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('tasks_pdf/', views.tasks_pdf, name='tasks_pdf'),
]
