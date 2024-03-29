"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #每次注册一个应用，都要注册一次总路由，找到相应的应用，再通过应用的路由找到相应的视图
    url(r'^', include('users.urls')),
    url(r'^oauth/', include('oauth.urls')),
    url(r'^', include('areas.urls')),
    url(r'^', include('goods.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('carts.urls')),
    url(r'^', include('orders.urls')),
    url(r'^', include('payments.urls'))


]
