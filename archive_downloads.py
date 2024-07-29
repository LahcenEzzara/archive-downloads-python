import os
import shutil
import datetime

# Set the path to the desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Set the path to the downloads folder
downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

# Get the current date and time in Morocco time
morocco_time = datetime.datetime.now().astimezone(
    datetime.timezone(offset=datetime.timedelta(hours=1)))
archive_date = morocco_time.strftime('archive_%d-%b-%Y_%Hh-%Mm-%Ss')

# Create a new folder with the current date and time as the name
archive_folder_path = os.path.join(desktop_path, 'archive', archive_date)

# Check if the archive folder already exists
if not os.path.exists(archive_folder_path):
    os.makedirs(archive_folder_path)

# Copy all files and folders from the downloads folder to the archive folder
for root, dirs, files in os.walk(downloads_path):
    relative_path = os.path.relpath(root, downloads_path)
    archive_root = os.path.join(archive_folder_path, relative_path)
    if not os.path.exists(archive_root):
        os.makedirs(archive_root)
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy2(file_path, archive_root)

# Print a success message
print(f"Downloads archived to {archive_folder_path}")

# Delete the archived files and folders from the downloads folder
for root, dirs, files in os.walk(downloads_path):
    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        shutil.rmtree(dir_path)

# Print a success message
print(f"Archived files and folders deleted from {downloads_path}")
