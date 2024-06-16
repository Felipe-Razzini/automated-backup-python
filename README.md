## Automated File Backup
This project automates the process of backing up a specified source directory to a destination directory.

## Features
1. Automated Backup: Automatically copies the contents of the source directory to the destination directory daily.
2. Timestamped Backups: Each backup is stored in a separate folder named with the current date, ensuring easy identification and organization of backups.
3. Error Handling: Handles scenarios where the destination directory already contains a backup for the current date.
4. Incremental Backups: Only backs up files that have changed since the last backup.
5. Compression: Compresses the backup files to save space.
