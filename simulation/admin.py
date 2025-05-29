from django.contrib import admin
from .models import SimulationRun


@admin.register(SimulationRun)
class SimulationRunAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'total_fault_current', 'protection_will_trip']
    list_filter = ['created_at', 'protection_will_trip', 'user']
    search_fields = ['id', 'user__username']
    readonly_fields = ['id', 'created_at']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('id', 'user', 'created_at')
        }),
        ('Input Parameters', {
            'fields': (
                'source_voltage', 'source_internal_resistance', 'line_resistance',
                'fault_resistance', 'fault_distance', 'num_substations',
                'substation_spacing', 'protection_trip_time', 'protection_trip_current',
                'system_inductance', 'line_inductance', 'simulation_time_step',
                'simulation_duration', 'line_length'
            )
        }),
        ('Results', {
            'fields': (
                'total_fault_current', 'energy_released', 'thermal_stress',
                'protection_will_trip', 'trip_time', 'shortest_distance_current',
                'longest_distance_current', 'shortest_distance_didt',
                'longest_distance_didt', 'peak_didt', 'steady_state_didt'
            )
        }),
        ('Files', {
            'fields': ('excel_file',)
        })
    )