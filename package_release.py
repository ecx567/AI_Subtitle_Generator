
import shutil
import os

source_dir = os.path.join("dist", "AutoSubtitles")
output_filename = os.path.join("dist", "AutoSubtitles_v1.0")

if os.path.exists(source_dir):
    print(f"Zipping {source_dir}...")
    shutil.make_archive(output_filename, 'zip', source_dir)
    print(f"Created {output_filename}.zip")
else:
    print(f"Source directory {source_dir} not found!")
