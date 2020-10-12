from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import screenview,findview
from django.views.generic import DetailView
from django.views import View
from .views import SearchData,LowToHigh,HighToLow,Female,Male

urlpatterns = [
    path('register',views.register,name="register" ),
    path('login',views.login,name="login" ),
    path('home',views.home,name="home" ),
    path('logout',views.logout,name="logout" ),
    path('index',views.index,name="index" ),
    path('bar',views.bar,name="bar" ),
    path('dele', views.dele, name="dele"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path("send",views.send,name="send"),
    path('data/',SearchData.as_view(),name='data'),
    path('LowToHigh/',LowToHigh.as_view(),name='lowtohigh'),
    path('HighToLow/',HighToLow.as_view(),name='hightolow'),
    path('searchfemale/',Female.as_view(),name='searchfemale'),
    path('searchmale/',Male.as_view(),name='searchmale'),
    path('screen/<int:pk>/',screenview.as_view(),name="detail"),
    #path('bg',views.bg,name="bg"),
    path('subprofile/<int:id>/',views.subprofile,name="subprofile"),
    path('locate',views.locate,name="locate"),
    path('review',views.review,name="review"),
    path('screen',views.screen,name="screen"),
    path('roomfind',views.roomfind,name="roomfind"),
    path('roomfind/<int:pk>/',findview.as_view(),name="findview"),
    path('homeshare',views.homeshare,name="homeshare"),
    path('profile',views.profile,name="profile"),
    path('owner',views.owner,name="owner"),
    path('',views.homepage,name="homepage"),
    path('reset_password',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('bg',views.bg,name="bg")
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
  #  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)