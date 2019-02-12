from django.contrib import admin

# Register your models here.
from apps.system.models import Party, AssemblyConstituencyName, District

admin.site.register(Party)
admin.site.register(AssemblyConstituencyName)
admin.site.register(District)
