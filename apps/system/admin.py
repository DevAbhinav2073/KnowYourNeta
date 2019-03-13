from django.contrib import admin

# Register your models here.
from apps.system.models import *


class PartyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Party._meta.fields]


class AssemblySegmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AssemblySegment._meta.fields]


class ConstituencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Constituency._meta.fields]


class StateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in State._meta.fields]


class VoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vote._meta.fields]


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]


class DistrictAdmin(admin.ModelAdmin):
    list_display = [field.name for field in District._meta.fields]


admin.site.register(Party, PartyAdmin)
admin.site.register(AssemblySegment, AssemblySegmentAdmin)
admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(District, DistrictAdmin)
