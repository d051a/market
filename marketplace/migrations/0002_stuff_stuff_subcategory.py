# Generated by Django 2.1.5 on 2019-02-12 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='stuff_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketplace.SubCategory'),
        ),
    ]