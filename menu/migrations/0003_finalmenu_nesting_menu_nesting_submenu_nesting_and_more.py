# Generated by Django 4.2.6 on 2023-10-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_finalmenu_remove_menu_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalmenu',
            name='nesting',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='nesting',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='nesting',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='finalmenu',
            name='sub_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finalmenu', to='menu.submenu'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenu', to='menu.menu'),
        ),
    ]
