from sxsw.models import Party
from django.contrib import admin

class PartyAdmin(admin.ModelAdmin):
	list_display = ('name', 'starttime')
	list_filter = ['starttime']
	search_fields = ['name']
	date_hierarchy = 'starttime'

admin.site.register(Party, PartyAdmin)         