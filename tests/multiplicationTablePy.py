#!python

import openpyxl
import sys

if len(sys.argv) != 2:
	print("Usage: ", sys.argv[0], " number")
	exit(0)
else:
	wb = openpyxl.Workbook()
	sheet = wb.active
	for i in range(0, int(sys.argv[1])):
		for j in range(1, int(sys.argv[1])+1):
			col = chr(ord('A')+i)
			sheet[col+str(j)] = j*(i+1)
			
	wb.save("table.xlsx")

