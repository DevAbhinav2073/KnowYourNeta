from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.authuser.models import PoliticianDetail, Supporter

User = get_user_model()


class PoliticianDetailInline(admin.StackedInline):
    model = PoliticianDetail
    max_num = 1


class SupporterInline(admin.StackedInline):
    model = Supporter


class AuthuserAdmin(UserAdmin):
    inlines = (PoliticianDetailInline, SupporterInline)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'fathers_name', 'date_of_birth', 'address', 'party', 'constituency', 'mobile_number', 'age',
                'user_type', 'username', 'password1', 'password2'),
        }),
    )


admin.site.register(User, AuthuserAdmin)
