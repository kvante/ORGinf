from django.contrib import admin
from .models import Organization, TopManager, FieldOfActivity, Link

admin.site.register(Organization)
admin.site.register(TopManager)
admin.site.register(FieldOfActivity)
admin.site.register(Link)
