from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

class SubMenu(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null=False, related_name='submenu')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

class FinalMenu(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=True, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    sub_menu = models.ForeignKey('SubMenu', on_delete=models.CASCADE, blank=False, null=False, related_name='finalmenu')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']