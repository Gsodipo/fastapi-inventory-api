import zipfile
import datetime
import os

# Set filenames
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
final_zip = f"complete-{timestamp}.zip"

files_to_include = [
    "unit_test_results.pdf",
    "README.txt"
]

# Automatically find latest database zip
latest_db_zip = sorted(
    [f for f in os.listdir() if f.startswith("database-") and f.endswith(".zip")],
    key=os.path.getmtime,
    reverse=True
)

if latest_db_zip:
    files_to_include.append(latest_db_zip[0])
else:
    print("⚠️ No database ZIP found. Skipping.")

# Create final zip
with zipfile.ZipFile(final_zip, 'w') as zipf:
    for file in files_to_include:
        if os.path.exists(file):
            zipf.write(file)
            print(f"Added: {file}")
        else:
            print(f"Missing file, not added: {file}")

print(f"\n Final ZIP created: {final_zip}")
