import os
import schedule
import datetime
import time
import shutil

source_dir = os.getenv("SOURCE_DIR")
destination_dir = os.getenv("DESTINATION_DIR")

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)