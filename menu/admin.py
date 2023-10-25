from django.contrib import admin

from .models import Menu, SubMenu, FinalMenu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'menu_id')
    list_display_links = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class FinalMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'sub_menu_id')
    list_display_links = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(FinalMenu, FinalMenuAdmin)

admin.site.site_header = 'Админ-панель MENU'