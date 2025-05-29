import os
import sys
from pathlib import Path
import mimetypes
from django.conf import settings # Assuming your Django settings are configured

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc_simulation.settings')

import django

django.setup()

import matplotlib

matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO


def test_chart_generation():
    """Test if matplotlib chart generation works"""
    print("Testing chart generation...")

    try:
        # Create a simple test chart
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title('Test Chart')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.grid(True)

        # Convert to base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        plt.close(fig)

        print("✅ Chart generation successful!")
        print(f"✅ Base64 string length: {len(graphic)}")
        return True

    except Exception as e:
        print(f"❌ Chart generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_simulation_model():
    """Test if simulation model works"""
    print("\nTesting simulation model...")

    try:
        from simulation.models import SimulationRun

        # Check if we have any simulation runs
        simulations = SimulationRun.objects.all()
        print(f"✅ Found {len(simulations)} simulation runs in database")

        if simulations:
            latest = simulations.first()
            print(f"✅ Latest simulation ID: {latest.id}")
            return latest.id
        else:
            print("⚠️  No simulation runs found. You need to run a simulation first.")
            return None

    except Exception as e:
        print(f"❌ Database query failed: {e}")
        return None


if __name__ == "__main__":
    test_chart_generation()
    test_simulation_model()

    # Configure Django settings if running standalone and settings are not yet configured
    # This might be necessary if settings.MEDIA_ROOT is used below and this script
    # is run outside of `manage.py shell` or `manage.py runserver`.
    # If you run this script with `python manage.py shell` and then import it,
    # or if you integrate this into a manage.py custom command,
    # Django settings will already be configured.
    # For a simple standalone test, you might need to set up a minimal Django environment.
    # However, for just mimetypes.guess_type with a filename string, Django setup is not strictly needed
    # unless you are dynamically constructing the path using settings.MEDIA_ROOT.

    # Option 1: Test with a hardcoded known filename (if you know one exists)
    # Make sure this path is correct and the file exists.
    # You might need to adjust the base path if MEDIA_ROOT is not set up here.
    # For simplicity, let's assume MEDIA_ROOT is 'C:/Users/lrich2/PycharmProjects/DC_ShortCircuit_Simulation/media'
    # and a file exists at 'charts/current_vs_time_some_id.png'

    # Construct an example filename based on your structure.
    # Replace with an *actual* filename from your media/charts directory.
    example_filename = "current_vs_time_32cdb260-441a-4510-8f89-471cf9acd740_1748324239.png"
    example_filepath_abs = os.path.join("C:\\Users\\lrich2\\PycharmProjects\\DC_ShortCircuit_Simulation\\media\\charts", example_filename)

    print(f"Testing filename: {example_filename}")
    guessed_type, encoding = mimetypes.guess_type(example_filename)
    print(f"Guessed type for '{example_filename}': {guessed_type}, Encoding: {encoding}")

    print(f"\nTesting absolute filepath: {example_filepath_abs}")
    # It's generally better to test with the URI or filename string, as that's what `static.serve` often gets.
    # However, testing with the full path can also be informative.
    # `mimetypes.guess_type` primarily works on the filename/URL, not file content.
    guessed_type_abs, encoding_abs = mimetypes.guess_type(example_filepath_abs)
    print(f"Guessed type for '{example_filepath_abs}': {guessed_type_abs}, Encoding: {encoding_abs}")

    # Test a common non-problematic PNG filename
    simple_png_filename = "test.png"
    guessed_type_simple, encoding_simple = mimetypes.guess_type(simple_png_filename)
    print(f"\nGuessed type for '{simple_png_filename}': {guessed_type_simple}, Encoding: {encoding_simple}")

    # List known MIME types to see if .png is registered correctly
    print(f"\nKnown types by mimetypes: {mimetypes.knownfiles}")
    print(f"Suffix map for .png: {mimetypes.suffix_map.get('.png', 'Not found')}")
    print(f"Types map for .png: {mimetypes.types_map.get('.png', 'Not found')}")
    print(f"Common types for .png: {mimetypes.common_types.get('.png', 'Not found')}")

    # If you have Django settings configured (e.g., running via manage.py shell):
    # try:
    #     from django.core.wsgi import get_wsgi_application
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc_simulation.settings')
    #     application = get_wsgi_application() # This configures Django settings
    #     from django.conf import settings
    #     charts_dir = os.path.join(settings.MEDIA_ROOT, 'charts')
    #     # Pick an actual file from your media/charts directory
    #     # For example, the first one found if the directory is not empty
    #     if os.path.exists(charts_dir) and os.listdir(charts_dir):
    #         actual_file_in_media = os.listdir(charts_dir)[0]
    #         if actual_file_in_media.endswith(".png"):
    #             print(f"\nTesting an actual file from media/charts: {actual_file_in_media}")
    #             guessed_type_actual, encoding_actual = mimetypes.guess_type(os.path.join(charts_dir, actual_file_in_media))
    #             print(f"Guessed type for '{actual_file_in_media}': {guessed_type_actual}, Encoding: {encoding_actual}")
    # except Exception as e:
    #     print(f"Could not fully initialize Django settings for deeper test: {e}")