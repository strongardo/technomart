"""
URL configuration for tehnomart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from home.views import home, feedback_form, search_form
from catalog.views import catalog
from django.conf import settings
from django.conf.urls.static import static
from users.views import register, add_to_cart, del_from_cart, cart
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_url'),
    path('catalog/', catalog, name='catalog_url'),
    path('feedback/', feedback_form, name='feedback_url'),
    path('search/', search_form, name='search_url'),
    path('register/', register, name='register_url'),
    path('login/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('del_from_cart/<int:product_id>', del_from_cart, name='del_from_cart'),
    path('cart', cart, name='cart_url')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

