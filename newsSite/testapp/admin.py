from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article


admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions', 'indented_title', 'id', 'lft', 'rght', 'tree_id', 'level', 'parent_id',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Article)