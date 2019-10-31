from django.contrib import admin
from .models import Office, Indicator, Dynamic


# Register your models here.
@admin.register(Office)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'city')
    list_filter = ('id', 'department', 'city')
    search_fields = ('id', 'department', 'city')
    exclude = ('slug',)
    ordering = ('id',)


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('group', 'name')
    list_filter = ('group', 'name')
    search_fields = ('group', 'name')
    ordering = ('name',)


@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ('month', 'office', 'indicator',  'value',)
    list_filter = ('month', 'value',)
    search_fields = ('month', 'value',)
    ordering = ('month', )


