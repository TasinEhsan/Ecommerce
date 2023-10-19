from django.urls import path
from apps import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('compare',views.compare,name='compare'),
    path('wishlist',views.wishlist,name='wishlist'),
]
