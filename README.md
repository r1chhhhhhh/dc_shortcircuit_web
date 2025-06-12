# DC Short Circuit Simulation Web Application

A convenient web-based simulation tool for analyzing DC short circuit conditions in electrical systems. This Django application provides engineers and students with an intuitive interface to model and analyze short circuit scenarios in DC power systems.

## Features

- **Interactive Web Interface**: User-friendly form-based input for simulation parameters
- **Real-time Calculations**: Comprehensive DC short circuit analysis including:
  - Total fault current calculation
  - Energy released during fault
  - Thermal stress analysis
  - Protection system evaluation
  - Time-domain analysis with di/dt calculations
- **Visual Results**: Interactive charts and graphs showing:
  - Current vs. time plots
  - di/dt analysis
  - Voltage drop calculations
- **Data Export**: Export simulation results to Excel format
- **Simulation History**: Track and manage previous simulation runs
- **Multi-substation Support**: Model systems with multiple contributing substations

## Technology Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Data Visualization**: Matplotlib
- **Data Processing**: NumPy, Pandas
- **Database**: SQLite (default Django database)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/r1chhhhhhh/dc_shortcircuit_web.git
   cd dc_shortcircuit_web
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django numpy pandas matplotlib openpyxl
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

### Running a Simulation

1. **Navigate to the Home Page**: Access the main simulation interface
2. **Input Parameters**: Fill in the simulation parameters including:
   - Source voltage and internal resistance
   - Line characteristics (resistance, inductance, length)
   - Fault parameters (resistance, distance)
   - Protection system settings
   - Simulation time parameters

3. **Execute Simulation**: Click "Run Simulation" to perform the analysis
4. **View Results**: Review the calculated results including:
   - Fault current values
   - Protection system response
   - Energy and thermal calculations
   - Interactive charts

5. **Export Data**: Download results in Excel format for further analysis

### Key Simulation Parameters

- **Source Voltage (VDC)**: System voltage level
- **Source Internal Resistance (Ω)**: Internal resistance of the power source
- **Line Resistance (Ω/km)**: Resistance per unit length of transmission line
- **Fault Resistance (Ω)**: Resistance at the fault location
- **Fault Distance (km)**: Distance from source to fault location
- **Number of Substations**: Contributing substations in the system
- **Protection Settings**: Trip current threshold and timing

## Project Structure

```
dc_shortcircuit_web/
├── dc_simulation/          # Django project settings
│   ├── settings.py         # Application configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── simulation/             # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic and calculations
│   ├── forms.py           # Django forms
│   ├── urls.py            # App-specific URLs
│   └── migrations/        # Database migrations
├── templates/              # HTML templates
│   └── base.html          # Base template
├── static/                 # Static files (CSS, JS)
├── manage.py              # Django management script
└── fix.py                 # Project structure validation
```

## Core Calculation Engine

The application includes a sophisticated calculation engine (`DCShortCircuitCalculation` class) that performs:

- **Multi-substation Analysis**: Determines current contribution from multiple sources
- **Time-domain Simulation**: Calculates transient and steady-state responses
- **Protection Analysis**: Evaluates protection system performance
- **Thermal Assessment**: Computes energy release and thermal stress

## API Endpoints

- `/` - Home page with simulation form
- `/run/` - Execute simulation
- `/results/<simulation_id>/` - View simulation results
- `/download/<simulation_id>/` - Download Excel results
- `/chart/<simulation_id>/<chart_type>/` - Get chart data
- `/history/` - View simulation history

## Testing

The project includes diagnostic tools:

- `fix.py` - Validates Django project structure
- `testchart.py` - Tests chart generation functionality

Run structure validation:
```bash
python fix.py
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source. Please check the repository for specific license terms.

## Support

For questions, issues, or contributions, please:
- Open an issue on GitHub
- Contact the repository maintainer
- Check the project documentation

## Acknowledgments

This tool is designed for educational and professional use in electrical engineering applications. It provides a practical interface for understanding DC short circuit phenomena and protection system behavior.