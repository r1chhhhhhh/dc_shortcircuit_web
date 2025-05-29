import os
from pathlib import Path


def check_project_files():
    """Check all files in the project directory"""

    base_dir = Path.cwd()
    print(f"Checking files in: {base_dir}")
    print("=" * 60)

    # Check media directory
    media_dir = base_dir / 'media'
    print(f"\n📁 MEDIA DIRECTORY: {media_dir}")
    if media_dir.exists():
        media_files = list(media_dir.rglob('*'))
        if media_files:
            for file in media_files:
                if file.is_file():
                    size_kb = file.stat().st_size / 1024
                    print(f"   📄 {file.relative_to(base_dir)} ({size_kb:.1f} KB)")
        else:
            print("   (empty)")
    else:
        print("   (doesn't exist)")

    # Check static directory
    static_dir = base_dir / 'static'
    print(f"\n📁 STATIC DIRECTORY: {static_dir}")
    if static_dir.exists():
        static_files = list(static_dir.rglob('*'))
        if static_files:
            for file in static_files:
                if file.is_file():
                    size_kb = file.stat().st_size / 1024
                    print(f"   📄 {file.relative_to(base_dir)} ({size_kb:.1f} KB)")
        else:
            print("   (empty)")

    # Look for any image files in the entire project
    print(f"\n🔍 SEARCHING FOR IMAGE FILES:")
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    image_files = []

    for ext in image_extensions:
        found = list(base_dir.rglob(f'*{ext}'))
        image_files.extend(found)

    if image_files:
        for img in image_files:
            size_kb = img.stat().st_size / 1024
            print(f"   🖼️  {img.relative_to(base_dir)} ({size_kb:.1f} KB)")
    else:
        print("   No image files found")

    # Check if test chart was created by our earlier test
    test_chart = base_dir / 'test_chart.png'
    if test_chart.exists():
        size_kb = test_chart.stat().st_size / 1024
        print(f"\n🧪 TEST CHART FOUND: test_chart.png ({size_kb:.1f} KB)")

    print("\n" + "=" * 60)
    print("📝 SUMMARY:")
    print("   - Charts are generated in memory, not saved as files")
    print("   - Charts are sent as base64 data to the web browser")
    print("   - No physical chart files are created by default")


if __name__ == "__main__":
    check_project_files()