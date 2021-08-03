from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
     path('',views.home,name="hm"),
     path('login/',views.login_view,name="login"),
     path('signup/',views.register_view,name="signup"),
     path('logout/',views.logout_view,name="logout"),
     path('sc/',views.schedule_view,name="sc"),
     path('book/',views.Book_view,name="bv"),
     path('tracker/',views.detector,name="dt"),
     path('info/',views.instruction,name="if"),


     
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)