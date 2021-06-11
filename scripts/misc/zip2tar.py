#! /usr/bin/env python
# Credit to Anthon on StackOverflow for the original script on Zip2tar
# Thread: https://unix.stackexchange.com/questions/146264/is-there-a-way-to-convert-a-zip-to-a-tar-without-extracting-it-to-the-filesystem
# Credit to ChrisProsser on StackOverflow for the original function on parsing directories
# Thread: https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python\

# Combining Author: Tim Schulz

import sys
import os
from zipfile import ZipFile, is_zipfile
import tarfile
import time

def parse_dirs(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if 'zip' in os.path.join(subdir, file):
                input_file_name = os.path.join(subdir, file)
                output_file_name = os.path.splitext(input_file_name)[0] + '.tar.gz'
                zip2tar(input_file_name, output_file_name)

def zip2tar(ifn, ofn):
    with ZipFile(ifn) as zipf:
        with tarfile.open(ofn, 'w:gz') as tarf:
            for zip_info in zipf.infolist():
                tar_info = tarfile.TarInfo(name=zip_info.filename)
                tar_info.size = zip_info.file_size
                add_vals = list(zip_info.date_time)
                add_vals.extend([-1,-1,-1])
                tar_info.mtime = time.mktime(tuple(add_vals))
                tarf.addfile(
                    tarinfo=tar_info,
                    fileobj=zipf.open(zip_info.filename)
                )

# Root of directory you want to change from zips to tar.gz
parse_dirs(sys.argv[1])
