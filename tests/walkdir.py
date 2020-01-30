#!/usr/bin/env python3

import os

for folderName, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)

    print('')
