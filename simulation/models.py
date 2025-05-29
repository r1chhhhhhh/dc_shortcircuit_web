from django.db import models
from django.contrib.auth.models import User
import uuid


class SimulationRun(models.Model):
    """Model to store simulation run results"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Input parameters
    source_voltage = models.FloatField(default=750.0)
    source_internal_resistance = models.FloatField(default=0.01)
    line_resistance = models.FloatField(default=0.02)
    fault_resistance = models.FloatField(default=0.01)
    fault_distance = models.FloatField(default=1.0)
    num_substations = models.IntegerField(default=3)
    substation_spacing = models.FloatField(default=5.0)
    protection_trip_time = models.FloatField(default=0.1)
    protection_trip_current = models.FloatField(default=4000)
    system_inductance = models.FloatField(default=0.001)
    line_inductance = models.FloatField(default=0.0005)
    simulation_time_step = models.FloatField(default=0.1)
    simulation_duration = models.FloatField(default=350.0)
    line_length = models.FloatField(default=10.0)
    
    # Results
    total_fault_current = models.FloatField(null=True, blank=True)
    energy_released = models.FloatField(null=True, blank=True)
    thermal_stress = models.FloatField(null=True, blank=True)
    protection_will_trip = models.BooleanField(default=False)
    trip_time = models.FloatField(null=True, blank=True)
    shortest_distance_current = models.FloatField(null=True, blank=True)
    longest_distance_current = models.FloatField(null=True, blank=True)
    shortest_distance_didt = models.FloatField(null=True, blank=True)
    longest_distance_didt = models.FloatField(null=True, blank=True)
    peak_didt = models.FloatField(null=True, blank=True)
    steady_state_didt = models.FloatField(null=True, blank=True)
    
    # File paths
    excel_file = models.FileField(upload_to='simulation_results/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Simulation {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"