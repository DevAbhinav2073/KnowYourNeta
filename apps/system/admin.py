from django.contrib import admin

# Register your models here.
from apps.system.models import Party, AssemblySegment, Constituency, State, Vote

admin.site.register(Party)
admin.site.register(AssemblySegment)
admin.site.register(Constituency)
admin.site.register(State)
admin.site.register(Vote)
