from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'verification', 'phone_number', 'news_count']
    actions = ['mark_as_verificated', 'mark_as_unverificated']

    def mark_as_verificated(self, request, queryset):
        if request.user.has_perm('users.can_verificate'):
            queryset.update(verification=True)
        else:
            raise PermissionDenied

    def mark_as_unverificated(self, request, queryset):
        if request.user.has_perm('users.can_verificate'):
            queryset.update(verification=False)
        else:
            raise PermissionDenied

    mark_as_verificated.short_description = 'Верифицировать пользователя'
    mark_as_unverificated.short_description = 'Деверифицировать'

admin.site.register(Profile,ProfileAdmin)
