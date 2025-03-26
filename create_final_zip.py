import zipfile
import datetime
import os

def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                # Skip virtual environment, .git, pycache
                if any(part in root for part in ['venv', '.git', '__pycache__']):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Zipped source folder to: {zip_name}")

# Set filenames
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
api_zip = f"api-source-{timestamp}.zip"
final_zip = f"complete-{timestamp}.zip"

# Step 1: Zip source code (excluding venv, .git, etc.)
zip_folder(".", api_zip)

# Step 2: Get latest database zip
latest_db_zip = sorted(
    [f for f in os.listdir() if f.startswith("database-") and f.endswith(".zip")],
    key=os.path.getmtime,
    reverse=True
)

files_to_include = [api_zip]

if latest_db_zip:
    files_to_include.append(latest_db_zip[0])
else:
    print(" No database ZIP found.")

# Step 3: Create final zip
with zipfile.ZipFile(final_zip, 'w') as zipf:
    for file in files_to_include:
        if os.path.exists(file):
            zipf.write(file)
            print(f" Added: {file}")
        else:
            print(f" Missing file, not added: {file}")

print(f"\n Final ZIP created: {final_zip}")
exit(0)

