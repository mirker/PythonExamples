#! python

import PyPDF2

print("1")
pdfFile = open('encrypted.pdf', 'rb')
keyFile = open('dictionary.txt', 'r')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

print("...")
cap = ''
for key in keyFile.readlines():
    if cap != key[0]:
        print(key[0])
        cap = key[0]
    key = key.rstrip('\r\n')
    if pdfReader.decrypt(key) != 0 or pdfReader.decrypt(key.lower()) != 0:
        print("Pdf file key is ", key)
        break

keyFile.close()
pdfFile.close()