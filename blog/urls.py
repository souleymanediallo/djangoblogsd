from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('<str:category>/', views.home, name="post_list"),
    path('detail/<int:post_id>/', views.post_detail, name="post_detail"),
    path('detail/<int:post_id>/<str:message>/', views.post_detail, name="post_detail_message"),

]