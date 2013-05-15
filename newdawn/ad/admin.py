from django.contrib import admin
from ad.models import Ad, Category


class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'position', 'keywords', 'enabled']
	actions = ['delete_selected']


admin.site.register(Category, CategoryAdmin)
