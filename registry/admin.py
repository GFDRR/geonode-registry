from registry.models import GeoNodeInstance,GeoNodeStatus,FaultyLayer
from django.contrib import admin

class GeoNodeInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at')

class GeoNodeStatusAdmin(admin.ModelAdmin):
    list_display = ('instance', 'layer_count', 'faulty_layers_count', 'map_count', 'faulty_maps', 'backup_date', 'created_at')

class FaultyLayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'instance', 'url', 'reason')

admin.site.register(GeoNodeInstance, GeoNodeInstanceAdmin)
admin.site.register(GeoNodeStatus, GeoNodeStatusAdmin)
admin.site.register(FaultyLayer, FaultyLayerAdmin)
