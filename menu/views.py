from django.views import View
from django.shortcuts import render


class MenuIndex(View):
    """The view class created for working site menus. He displaing menu, submenu and under the submenu"""
    
    
    def get_context_data(self, *, object_list=None, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title': 'INDEX']
        return context

    
    def get(self, request, *args, **kwargs):
        request.menu_slug = kwargs.get('menu_slug', None)
        request.submenu_slug = kwargs.get('submenu_slug', None)
        request.finalmenu_slug = kwargs.get('finalmenu_slug', None)
        return render(request, 'menu/index.html')