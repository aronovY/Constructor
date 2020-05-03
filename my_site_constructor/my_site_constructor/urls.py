"""my_site_constructor URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from authentication import views as auth_view
from constructor import views, views_constructor

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '',
        auth_view.LoginView.as_view(),
        name='login'),

    path(
        'login/',
        auth_view.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_view.LogoutView.as_view(),
        name='logout',
    ),

    path(
        'register/',
        auth_view.RegisterFormView.as_view(),
        name='register',
    ),
    path(
        'home/',
        views.home,
        name='home'),

    path(
        'home/settings',
        views.settings,
        name='settings'),

    path(
        'home/settings/history',
        views.history,
        name='history'),

    path('parts/',
         views.parts_view,
         name='parts'),

    path(
        'parts/products/<int:category>',
        views.ProdListView.as_view(),
        name='product-list'
    ),

    path(
        'parts/products/<int:category>/<int:pk>/',
        views.DetailView.as_view(),
        name='detail'
    ),

    path(
        'constructor/',
        views_constructor.start_constructor,
        name='start-constructor'
    ),

    path(
        'constructor/select_component/<int:id>/<str:manufacturer>',
        views_constructor.FirstSelectLisView.as_view(),
        name='first-component'
    ),

    path(
        'constructor/second_component/<int:id>/<int:component>',
        views_constructor.SecondSelectLisView.as_view(),
        name='second-component'
    ),

    path(
        'constructor/third_component/<int:id>/<int:component>',
        views_constructor.ThirdSelectLisView.as_view(),
        name='third-component'
    ),

    path(
        'constructor/which_video_card/<int:id>/<int:component>',
        views_constructor.which_video_card,
        name='choice_video'
    ),

    path(
        'constructor/fourth_component/<int:id>/<str:card>-<str:memory>/',
        views_constructor.FourthSelectLisView.as_view(),
        name='fourth-component'
    ),

    path(
        'constructor/fifth_component/<int:id>/<int:component>',
        views_constructor.FifthSelectLisView.as_view(),
        name='fifth-component'
    ),

    path(
        'constructor/sixth_component/<int:id>/<int:component>',
        views_constructor.SixthSelectLisView.as_view(),
        name='sixth-component'
    ),

    path(
        'constructor/which_power/<int:id>/<int:component>',
        views_constructor.which_power,
        name='choice_power_case'
    ),

    path(
        'constructor/seventh_component/<int:id>/<int:component>/',
        views_constructor.SeventhSelectLisView.as_view(),
        name='seventh-component'
    ),

    path(
        'constructor/eighth_component/<int:id>/<int:component>/<str:block>/',
        views_constructor.EighthSelectLisView.as_view(),
        name='eighth-component'
    ),

    path(
        'constructor/dvd_choice/<int:case_id>/<int:component>',
        views_constructor.choice_dvd,
        name='dvd-choice'
    ),

    path(
        'constructor/ninth_component/<int:id>/<str:choice>/',
        views_constructor.NinthSelectLisView.as_view(),
        name='ninth-component'
    ),

    path(
        'constructor/end_constructor/<int:id>/<int:component>/<str:choice>/',
        views_constructor.EndConstructorView.as_view(),
        name='end-constructor'
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
