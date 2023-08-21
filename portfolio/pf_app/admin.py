from django.contrib import admin
from . import models

# admin.site.register(models.Experience)
# admin.site.register(models.Education)


# admin of section "CAREER AND EDUCATION"
@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name_organization', 'position', 'start_at', 'end_at')
    list_filter = ('name_organization', 'position', 'start_at')
    search_fields = ('name_organization', 'position')


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name_organization', 'major', 'start_at', 'end_at')
    list_filter = ('name_organization', 'major', 'start_at')
    search_fields = ('name_organization', 'major')
