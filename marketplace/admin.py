from django.contrib import admin
from .models import Stuff, User, Category, SubCategory, City

admin.site.register(Category)
admin.site.register(User)
admin.site.register(City)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ['category']


class StuffAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'visible', 'moderated')
    list_filter = ['visible', 'moderated','tags']


admin.site.register(Stuff, StuffAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)