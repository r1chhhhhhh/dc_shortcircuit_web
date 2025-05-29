from django import forms
from .models import SimulationRun


class SimulationForm(forms.ModelForm):
    """Form for simulation input parameters"""
    
    class Meta:
        model = SimulationRun
        fields = [
            'source_voltage', 'source_internal_resistance', 'line_resistance',
            'fault_resistance', 'fault_distance', 'num_substations',
            'substation_spacing', 'protection_trip_time', 'protection_trip_current',
            'system_inductance', 'line_inductance', 'simulation_time_step',
            'simulation_duration', 'line_length'
        ]
        
        widgets = {
            'source_voltage': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.01', 'min': '0'
            }),
            'source_internal_resistance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.001', 'min': '0'
            }),
            'line_resistance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.001', 'min': '0'
            }),
            'fault_resistance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.001', 'min': '0'
            }),
            'fault_distance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.1', 'min': '0'
            }),
            'num_substations': forms.NumberInput(attrs={
                'class': 'form-control', 'min': '1'
            }),
            'substation_spacing': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.1', 'min': '0'
            }),
            'protection_trip_time': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.01', 'min': '0'
            }),
            'protection_trip_current': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '1', 'min': '0'
            }),
            'system_inductance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.0001', 'min': '0'
            }),
            'line_inductance': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.0001', 'min': '0'
            }),
            'simulation_time_step': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.01', 'min': '0.01'
            }),
            'simulation_duration': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '1', 'min': '1'
            }),
            'line_length': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.1', 'min': '0'
            }),
        }
        
        labels = {
            'source_voltage': 'Source Voltage (VDC)',
            'source_internal_resistance': 'Source Internal Resistance (Ohms)',
            'line_resistance': 'Line Resistance (Ohms/km)',
            'fault_resistance': 'Fault Resistance (Ohms)',
            'fault_distance': 'Fault Distance (km)',
            'num_substations': 'Number of Substations',
            'substation_spacing': 'Substation Spacing (km)',
            'protection_trip_time': 'Protection Trip Time (seconds)',
            'protection_trip_current': 'Protection Current Threshold (A)',
            'system_inductance': 'System Inductance (H)',
            'line_inductance': 'Line Inductance (H/km)',
            'simulation_time_step': 'Simulation Time Step (ms)',
            'simulation_duration': 'Simulation Duration (ms)',
            'line_length': 'Total Line Length (km)',
        }