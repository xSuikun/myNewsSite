from django.contrib import admin
from .models import Rubric


class RubricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lft', 'rght', 'tree_id', 'level', 'parent_id')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Rubric, RubricAdmin)

admin.site.site_title = 'Управление рубриками'
admin.site.site_header = 'Управление рубриками'
