from django.contrib import admin
from .models import ReDicKoatuuRegion, ReDistrict, RegionCenter, CenterRegional


# Register your models here.


@admin.register(ReDicKoatuuRegion)
class ReDicKoatuuRegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'this_id')
    ordering = [
        "name",
    ]


@admin.register(ReDistrict)
class ReCityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'level', 'this_id')
    ordering = [
        "name",
    ]
    list_filter = [
        "region",
    ]


@admin.register(RegionCenter)
class RegionCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'level', 'this_id')
    ordering = [
        "name",
    ]
    list_filter = [
        'district'
    ]
