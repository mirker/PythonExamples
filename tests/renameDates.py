#!/usr/bin/env python3

import shutil, os, re

# Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)    # All the text before the date
                        ((0|1)?\d)-   # one or two digit for the month
                        ((0|1|2|3)?\d)- # one or two digit for the day
                        ((19|20)\d\d)  # four digits for the year
                        (.*?)$         # all text after the date
                         """, re.VERBOSE)

# Loop over the file in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip file without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # Form the European-style filename

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    # shutil.move(amerFilename, euroFilename) # uncomment after testing
