from django.urls import path

from .views import (
    home,
    login_page,
    register_page,
    dashboard_page,
    history_page,
    generate_page,
    logout_page
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'login/',
        login_page,
        name='login'
    ),

    path(
        'register/',
        register_page,
        name='register'
    ),

    path(
        'dashboard/',
        dashboard_page,
        name='dashboard'
    ),

    path(
        'history/',
        history_page,
        name='history'
    ),

    path(
        'generate/',
        generate_page,
        name='generate'
    ),

    path(
    'logout/',
    logout_page,
    name='logout'
    ),
]