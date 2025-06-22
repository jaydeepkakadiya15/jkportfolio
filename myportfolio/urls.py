"""
URL configuration for myportfolio project.

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
from userapp.views import index
from adminapp.views import *
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),


    path('adminapp/admin_register/', register, name='admin_register'),
    path('adminapp/admin_login/', admin_login, name='admin_login'),
    path('adminapp/admin_logout/', admin_logout, name='admin_logout'),

    path('adminapp/dashboard/', dashboard, name='dashboard'),
    path('adminapp/add_data/', add_data, name='add_data'),
    path('adminapp/view_data/', view_data, name='view_data'),
    path('adminapp/edit_data/<int:id>/', edit_data, name='edit_data'),
    path('adminapp/delete_data/<int:id>/', delete_data, name='delete_data'),

    path('adminapp/add_bio/', add_bio, name='add_bio'),
    path('adminapp/view_bio/', view_bio, name='view_bio'),
    path('adminapp/edit_bio/<int:id>/', edit_bio, name='edit_bio'),
    path('adminapp/delete_bio/<int:id>/', delete_bio, name='delete_bio'),

    path('adminapp/add_banner/', add_banner, name='add_banner'),
    path('adminapp/view_banner/', view_banner, name='view_banner'),
    path('adminapp/edit_banner/<int:id>/', edit_banner, name='edit_banner'),
    path('adminapp/delete_banner/<int:id>/', delete_banner, name='delete_banner'),

    path('adminapp/add_skill/', add_skill, name='add_skill'),
    path('adminapp/view_skill/', view_skill, name='view_skill'), 
    path('adminapp/edit_skill/<int:id>/', edit_skill, name='edit_skill'),
    path('adminapp/delete_skill/<int:id>/', delete_skill, name='delete_skill'),

    path('adminapp/add_education/', add_education, name='add_education'),
    path('adminapp/view_education/', view_education, name='view_education'),
    path('adminapp/edit_education/<int:id>/', edit_education, name='edit_education'),
    path('adminapp/delete_education/<int:id>/', delete_education, name= 'delete_education'),

    path('adminapp/add_ex/', add_experience, name='add_experience'),
    path('adminapp/view_ex/', view_experience, name='view_experience'),
    path('adminapp/edit_ex/<int:id>/', edit_experience, name='edit_experience'),
    path('adminapp/delete_ex/<int:id>/', delete_experience, name='delete_experience'),

    path('adminapp/add_portfolio/', add_portfolio, name='add_portfolio'),
    path('adminapp/view_portfolio/', view_portfolio, name='view_portfolio'),
    path('adminapp/edit_portfolio/<int:id>/', edit_portfolio, name='edit_portfolio'),
    path('adminapp/delete_portfolio/<int:id>/', delete_portfolio, name='delete_portfolio'),

    path('adminapp/add_service/', add_service, name='add_service'),
    path('adminapp/view_service/', view_service, name='view_service'),
    path('adminapp/edit_service/<int:id>', edit_service, name='edit_service'),
    path('adminapp/delete_service/<int:id>', delete_service, name='delete_service'),

    path('adminapp/view_user_contact/', view_user_contact, name='view_user_contact'),
    path('adminapp/delete_user_contact/<int:id>', delete_user_contact, name='delete_user_contact'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
