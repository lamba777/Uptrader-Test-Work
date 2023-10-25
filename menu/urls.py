from django.urls import path

from .views import MenuIndex

urlpatterns = [
    path('api/v1/index/', MenuIndex.as_view(), name='index'),
    path('api/v1/<slug:menu_slug>/', MenuIndex.as_view(), name='expanded_menu'),
    path('api/v1/<slug:menu_slug>/<slug:submenu_slug>/', MenuIndex.as_view(), name='submenu_page'),
    path('api/v1/<slug:menu_slug>/<slug:submenu_slug>/<slug:finalmenu_slug>/', MenuIndex.as_view(), name='finalmenu_page')
]