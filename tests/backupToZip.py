#!/usr/bin/env python3
# copies an entrie folder and it conents to
# a ZIP file whose filename increments
import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on
    # waht files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number+1

    # Create the zip file
    print('Creating %s ...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Walk the entre folder tree and compress the file in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # add the current folder to the zip file
        backupZip.write(foldername)
        # add all the files in the folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backupToZip('/home/henry/study/python')

