from django.core.exceptions import PermissionDenied
from .models import News, Comments, Tags
from django.contrib import admin


class CommentsInline(admin.TabularInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    inlines = (CommentsInline, )
    list_display = ['id', 'title', 'created', 'updated', 'active']
    list_filter=['active']
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        if request.user.has_perm('news_and_comments.can_publicate'):
            queryset.update(active=True)
        else:
            raise PermissionDenied

    def mark_as_inactive(self, request, queryset):
        if request.user.has_perm('news_and_comments.can_publicate'):
            queryset.update(active=False)
        else:
            raise PermissionDenied

    mark_as_active.short_description = 'Сделать новость активной'
    mark_as_inactive.short_description = 'Сделать новость неактивной'


class CommentsAdmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = [field.name for field in Comments._meta.get_fields()]
    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(text='Удалено администратором')

    delete_by_admin.short_description = 'Удалить комментарий от администратора'


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Tags, TagsAdmin)
