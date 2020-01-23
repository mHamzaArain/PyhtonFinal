import PyPDF4 as pdf

# pdf = open(<PDF.pdf>, 'rb')   # To read file 
# reader.numPages                   # no. of pages
# page = reader.getPage(4)      # get page 4
# page.extractText()                   # extract as formatted text

# reader1 = pdf.PdfFileReader(pdfFile1)     # Read Every text in file
# writer = pdf.PdfFileWriter()                       # Empty obj to  write new file
# writer.addPage(page)                                # Take str and save as page wise
# writer.write(outFile)                                    # saved str to write in file  
# pdfFile.close()                                             # To close pdf files

# #################Read: Print all pages in pdf
# pdfFile = open(r'C:\Users\Family\Desktop\m.pdf', 'rb')
# reader = pdf.PdfFileReader(pdfFile)
# for numPage in range(reader.numPages):
# 	print(reader.getPage(numPage).extractText())
# pdfFile.close()

# #################Write: Merge pdf files to make new
# pdfFile1 = open(r'C:\Users\Family\Desktop\m1.pdf', 'rb')
# pdfFile2 = open(r'C:\Users\Family\Desktop\m2.pdf', 'rb')

# # Read Pdf files
# reader1 = pdf.PdfFileReader(pdfFile1)
# reader2 = pdf.PdfFileReader(pdfFile2)

# # Object to write
# writer = pdf.PdfFileWriter()

# # Writing pdf file1 pages to writer object
# for pageNum in range(reader1.numPages):
# 	page = reader1.getPage(pageNum)
# 	writer.addPage(page)
	
# # Writing pdf file2 pages to writer object
# for pageNum in range(reader2.numPages):
# 	page = reader2.getPage(pageNum)
# 	writer.addPage(page)

# # make new pdf file and write everything in writer obj
# outFile = open('new.pdf', 'wb')
# writer.write(outFile)

# # Close both files
# pdfFile1.close()
# pdfFile2.close()