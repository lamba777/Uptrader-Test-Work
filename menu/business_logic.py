def create_menu_structure(queryset):
    """
    The custom method which making a structured menu from query
    
    Args:
        queryset (django.db.models.query.QuerySet): The queryset is used for creating with his help a structured site menu
    
    Returns:
        menu_structure: A structured site menu
    """
    
    menu_structure = {}

    for final_menu in queryset:
        menu = final_menu.sub_menu.menu
        sub_menu = final_menu.sub_menu

        if menu not in menu_structure:
            menu_structure[menu] = {}

        if sub_menu not in menu_structure[menu]:
            menu_structure[menu][sub_menu] = []
            
        menu_structure[menu][sub_menu].append(final_menu)
    
    return menu_structure