import gdown
import os
import sys

# Get the Google Drive link from the environment variable
url = "https://drive.google.com/drive/folders/1-tktqeXhjjvpACRWHd9xE2UgDzpt4aco?usp=drive_link"

if not url:
    print("\n❌ Error: GDRIVE_LINK environment variable is not set.")
    sys.exit(1)

# The name of the file to be saved inside the container
# This will be saved inside the /app directory
output_filename = os.environ.get('OUTPUT_FILENAME', 'downloaded_files.zip')

print(f"🚀 Starting download from Google Drive link...")
print(f"   Saving to: {output_filename}")

# The magic line: Download the file using gdown
gdown.download(url=url, output=output_filename, quiet=False)

print(f"\n✅ Download complete!")
