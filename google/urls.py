from django.urls import path
from .views import AboutPageViews,HomePageViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomePageViews.as_view(), name='home' ),
    path('about/', AboutPageViews.as_view(),name='about-us'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

