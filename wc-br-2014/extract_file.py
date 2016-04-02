# coding: utf-8

import os
import zipfile
import sys

def main(path):
    if not os.path.exists(path):
        print('File {0} does not exists!'.format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("All files extracted")

if __name__ == "__main__":
    main(sys.argv[1])
