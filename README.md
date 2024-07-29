# Archive Downloads Script

A Python script that archives downloads from the `Downloads` folder to a new folder on the desktop, with a unique name based on the current date and time.

## Features

- Archives downloads from the `Downloads` folder to a new folder on the desktop
- Creates a unique folder name based on the current date and time
- Copies all files and folders from the `Downloads` folder to the new archive folder
- Deletes the archived files and folders from the `Downloads` folder

## Requirements

- Python 3.x
- Windows 10 (or later)

## Usage

1. Save this script as `archive_downloads.py`
2. Create a new batch file `run_archive.bat` with the following contents:

```batch
@echo off
echo Starting script...
py "archive_downloads.py"
echo Script finished. Press any key to exit...
pause
```

3. Run the batch file by double-clicking on it
4. The script will archive the downloads and delete the archived files and folders from the `Downloads` folder

## License

This project is licensed under the MIT License.

**© 2024 Lahcen Ezzara. All rights reserved.**