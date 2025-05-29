import os
import sys
from pathlib import Path


def test_django_structure():
    """Test if Django structure is correct"""

    base_dir = Path.cwd()

    required_files = [
        'manage.py',
        'dc_simulation/__init__.py',
        'dc_simulation/settings.py',
        'dc_simulation/urls.py',
        'dc_simulation/wsgi.py',
        'simulation/__init__.py',
        'simulation/models.py',
        'simulation/views.py',
        'simulation/urls.py',
        'simulation/admin.py',
        'simulation/apps.py',
        'simulation/migrations/__init__.py',
        'templates/base.html',
        'static/css/style.css'
    ]

    print("Checking Django project structure...")
    print("=" * 50)

    missing_files = []
    for file_path in required_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} - MISSING")
            missing_files.append(file_path)

    print("=" * 50)

    if missing_files:
        print(f"❌ Missing {len(missing_files)} files:")
        for file in missing_files:
            print(f"   - {file}")
    else:
        print("✅ All required files present!")

        # Test Django import
        try:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc_simulation.settings')
            import django
            django.setup()
            print("✅ Django setup successful!")
            return True
        except Exception as e:
            print(f"❌ Django setup failed: {e}")
            return False

    return False


if __name__ == "__main__":
    test_django_structure()