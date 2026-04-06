"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# import rander
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
#
def home1(request):
    name = request.Get.get('name')
#
#     # return HttpResponse("<h1>hello</h1>")
    return render(request, 'home1.html', context={"name": "miraziz" })
#
# def not_found(request):
#     return render(request, '404_not_found.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('', home),
    path('products/', include('product.urls')),

    # path('',home1),
    # path('404',not_found),
]
