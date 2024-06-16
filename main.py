import os
import schedule
import datetime
import time
import shutil
import zipfile

source_dir = os.getenv("SOURCE_DIR")
destination_dir = os.getenv("DESTINATION_DIR")

def incremental_backup_and_compress(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        exit_status = os.system(f'rsync -a --delete {source}/ {dest_dir}/')
        if exit_status != 0:
            print(f"rsync command failed with exit status: {exit_status}")
        else:
            shutil.make_archive(dest_dir, 'zip', dest_dir)
            print(f"Backup and compression completed for: {dest_dir}")
    except FileNotFoundError:
        print(f"Directory not found: {source} or {dest_dir}")
    except Exception as e:
        print(f"An error occurred during the backup and compression process: {e}")

incremental_backup_and_compress(source_dir, destination_dir)
