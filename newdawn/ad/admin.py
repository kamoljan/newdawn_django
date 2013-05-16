from django.contrib import admin
from ad.models import Ad, Category


class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'position', 'keywords', 'enabled']
	actions = ['delete_selected']


class AdAdmin(admin.ModelAdmin):
	list_display = ('id', 'subject',
	                'user_email', 'user_phone',
	                'user_ip',
	                'category', 'created_time',
	                'updated_time',
	                'ad_status')
	search_fields = ('subject', 'user_email')
	list_filter = ('ad_status', )
	actions_on_top = True
	actions_on_bottom = True
	save_on_top = True
	list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)