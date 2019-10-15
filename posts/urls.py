from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='home'),
    path('accounts/login/',
         auth_view.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('accounts/signup/',
         views.BlogSignUp.as_view(), name='signup'),
    path('accounts/logout/',
         auth_view.LogoutView.as_view(template_name='posts/logout.html'), name='logout'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogNewPostView.as_view(), name='new_post'),
    path('post/<int:pk>/update',
         views.BlogUpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/Delete',
         views.BlogDeletePostView.as_view(), name='delete_post'),

]
