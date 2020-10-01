#!/usr/bin/python

import sys, os
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path):
	fname = os.path.splitext(os.path.basename(path))[0]

	pdf = PdfFileReader(path)
    pages = pdf.getNumPages()

    for page in range(pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = './temp/{}.pdf'.format(page+1)
        
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            
        #print('Created: {}'.format(output_filename))
    print('Pdf is splitted')

if __name__ == '__main__':
    #path = sys.argv[1]
    print("Enter your file:")
    path = input()

    pdf_splitter('./archive/' + path)