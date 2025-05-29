from django.urls import path
from . import views

app_name = 'simulation'

urlpatterns = [
    path('', views.simulation_home, name='home'),
    path('run/', views.run_simulation, name='run'),
    path('results/<uuid:simulation_id>/', views.simulation_results, name='results'),
    path('download/<uuid:simulation_id>/', views.download_excel, name='download_excel'),
    path('chart/<uuid:simulation_id>/<str:chart_type>/', views.get_chart, name='get_chart'),
    path('history/', views.simulation_history, name='history'),
]