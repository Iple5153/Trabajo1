from django.conf.urls import url, include
from django.contrib import admin
from Iple import views as Iple_views


urlpatterns = [
      url(r'^account/', include("accounts.urls")),
      url(r'^$',Iple_views.login_redirect, name='login_redirect'),
      url(r'^admin/', admin.site.urls),
      
      
]