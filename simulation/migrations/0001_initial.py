# Generated migration file
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationRun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('source_voltage', models.FloatField(default=750.0)),
                ('source_internal_resistance', models.FloatField(default=0.01)),
                ('line_resistance', models.FloatField(default=0.02)),
                ('fault_resistance', models.FloatField(default=0.01)),
                ('fault_distance', models.FloatField(default=1.0)),
                ('num_substations', models.IntegerField(default=3)),
                ('substation_spacing', models.FloatField(default=5.0)),
                ('protection_trip_time', models.FloatField(default=0.1)),
                ('protection_trip_current', models.FloatField(default=4000)),
                ('system_inductance', models.FloatField(default=0.001)),
                ('line_inductance', models.FloatField(default=0.0005)),
                ('simulation_time_step', models.FloatField(default=0.1)),
                ('simulation_duration', models.FloatField(default=350.0)),
                ('line_length', models.FloatField(default=10.0)),
                ('total_fault_current', models.FloatField(blank=True, null=True)),
                ('energy_released', models.FloatField(blank=True, null=True)),
                ('thermal_stress', models.FloatField(blank=True, null=True)),
                ('protection_will_trip', models.BooleanField(default=False)),
                ('trip_time', models.FloatField(blank=True, null=True)),
                ('shortest_distance_current', models.FloatField(blank=True, null=True)),
                ('longest_distance_current', models.FloatField(blank=True, null=True)),
                ('shortest_distance_didt', models.FloatField(blank=True, null=True)),
                ('longest_distance_didt', models.FloatField(blank=True, null=True)),
                ('peak_didt', models.FloatField(blank=True, null=True)),
                ('steady_state_didt', models.FloatField(blank=True, null=True)),
                ('excel_file', models.FileField(blank=True, null=True, upload_to='simulation_results/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]