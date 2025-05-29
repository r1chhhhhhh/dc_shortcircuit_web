import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc_simulation.settings')
django.setup()

from simulation.models import SimulationRun
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import shutil
from pathlib import Path


def clear_all_simulation_data():
    """Clear all simulation data from database, sessions, and files"""

    print("🧹 Starting to clear all simulation data...")

    # 1. Clear database records
    print("\n📊 Clearing database records...")
    simulation_count = SimulationRun.objects.count()
    print(f"Found {simulation_count} simulation records in database")

    if simulation_count > 0:
        SimulationRun.objects.all().delete()
        print(f"✅ Deleted {simulation_count} simulation records")
    else:
        print("ℹ️  No simulation records found in database")

    # 2. Clear session data
    print("\n🔐 Clearing session data...")
    sessions = Session.objects.all()
    calculator_sessions_count = 0

    for session in sessions:
        store = SessionStore(session_key=session.session_key)
        data = store.load()

        # Check if session has calculator data
        calculator_keys = [k for k in data.keys() if k.startswith('calculator_')]

        if calculator_keys:
            calculator_sessions_count += len(calculator_keys)
            # Clear calculator data from session
            for key in calculator_keys:
                del data[key]

            # Save the updated session
            store.update(data)
            store.save()

    print(f"✅ Cleared {calculator_sessions_count} calculator sessions")

    # 3. Clear uploaded files
    print("\n📁 Clearing uploaded files...")
    media_path = Path('media/simulation_results')

    if media_path.exists():
        file_count = len(list(media_path.glob('*')))
        if file_count > 0:
            shutil.rmtree(media_path)
            media_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Deleted {file_count} files from media directory")
        else:
            print("ℹ️  No files found in media directory")
    else:
        print("ℹ️  Media directory doesn't exist")

    # 4. Clear SQLite database file (optional - only if using SQLite)
    print("\n🗃️  Database file info:")
    db_path = Path('db.sqlite3')
    if db_path.exists():
        size_mb = db_path.stat().st_size / (1024 * 1024)
        print(f"Database file size: {size_mb:.2f} MB")
        print("Note: Database file still exists but simulation data has been cleared")

    print("\n🎉 All simulation data cleared successfully!")
    print("📋 Summary:")
    print(f"   - Database records: {simulation_count} deleted")
    print(f"   - Session data: {calculator_sessions_count} calculator sessions cleared")
    print("   - Media files: Cleared")


if __name__ == "__main__":
    confirm = input("⚠️  This will delete ALL simulation data. Are you sure? (type 'yes' to confirm): ")

    if confirm.lower() == 'yes':
        clear_all_simulation_data()
    else:
        print("❌ Operation cancelled")