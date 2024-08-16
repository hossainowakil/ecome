
from django.contrib import admin
from django.urls import path
from management.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name = "home"),
    path('contact/',contact,name="contact"),
    path('detail/<int:id>/',detail,name="detail"),
    path('add_contact/' , add_contact, name="add_contact"),
    path('delete_contact/<int:id>', delete_contact, name="delete_contact"),
    path('edit_contact/<int:id>/',edit_contact,name="edit_contact"),

    path('profile/', profile , name = "profile"),
    path('sign_in/', sign_in, name="sign_in"),
    path('sign_up/', sign_up,name= "sign_up")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
