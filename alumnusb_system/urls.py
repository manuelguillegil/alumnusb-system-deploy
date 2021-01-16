"""alumnusb_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from main import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^personal_data/$', views.user_data, name = 'Datos Personales'),
    url(r'^personal_data/edit/(?P<username>[\w.@+-]+)/$', accounts_views.edit_user_data, name = 'edit_user_data'),

    url(r'^personal_data/get/(?P<username>[\w.@+-]+)/$', accounts_views.get_user_data, name = 'Get User Data'),

    url(r'^personal_data/edit_test/(?P<username>[\w.@+-]+)/$', accounts_views.edit_user_data_test, name = 'edit_user_data_test'), #esta es de prueba, se quita

    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    ## Estos son para probar mis cosas, ARREGLAR ESTO DESPUES xD
    path('accounts/',include('accounts.urls'))
]
