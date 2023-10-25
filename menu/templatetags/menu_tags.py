from django import template
from menu.models import FinalMenu
from menu.business_logic import create_menu_structure


register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, *args):
    """
    The template tag method. Returns a structured menu and its context.

    Args:
        context (django.template.context.RequestContext): The context is used for getting slugs from the URL query.
        args (tuple): The args are used to filter the menu by their name.

    Returns:
        dict: A custom context to help display menus.
    """
        
    menu_slug = context['request'].menu_slug
    submenu_slug = context['request'].submenu_slug
    finalmenu_slug = context['request'].finalmenu_slug
    
    if not args:
        queryset = FinalMenu.objects.select_related('sub_menu__menu')
    else:
        queryset = FinalMenu.objects.select_related('sub_menu__menu').filter(sub_menu__menu__name__in=args)

    structured_menu = create_menu_structure(queryset)
    
    template_tag_context = {
        'structured_menu': structured_menu, 
        'menu_slug': menu_slug, 
        'submenu_slug': submenu_slug, 
        'finalmenu_slug': finalmenu_slug,
    }  
    
    return template_tag_context