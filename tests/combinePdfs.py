#! python

import PyPDF2, os

# Get all the PDF filesnames
pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=lambda y: y.lower())
print(pdfFiles)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    try:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print("add ", filename)
        # Loop through all the pages(except the first) and add them
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    except Exception:
        print('Continue')
    finally:
        pass #pdfFileObj.close()

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()