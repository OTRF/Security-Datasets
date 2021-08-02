import glob
import yaml
import os

current_directory = os.path.dirname(__file__)
datasets_directory = os.path.join(current_directory, "..", "datasets")
metadata_directory = os.path.join(datasets_directory, "metadata")
metadata2_directory = os.path.join(datasets_directory, "metadata2")

print("[+] Opening metadata yaml files..")
print(metadata_directory)
metadata_files = glob.glob(os.path.join(metadata_directory, "*.yaml"))
metadata_loaded = [yaml.safe_load(open(metadata_file, encoding="utf8").read()) for metadata_file in metadata_files]

for yf in metadata_loaded:
    if 'type' in yf:
        print(yf['id'])