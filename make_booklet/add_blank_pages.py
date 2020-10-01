#!/usr/bin/python

import sys, os
from PyPDF2 import PdfFileReader, PdfFileWriter

def add_blank(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pages = pdf.getNumPages()

    path_blank_page = './white_page.pdf'
    blank_page = PdfFileReader(path_blank_page)

    print('Pages: ' + str(pages))

    if (pages%4) == 0:
        print('Pages are already a multiple of 4')

        return pages

    else:
        os.mkdir('temp')
        while True:
            missing = pages%4
            pages = pages + 1
            
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(blank_page.getPage(0))
            output_filename = './temp/{}.pdf'.format(pages)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            print('Add blank page: {}'.format(output_filename))

            if (pages%4) == 0:
                break
        print('Pages are now a multiple of 4')

        return pages

if __name__ == '__main__':
    # path = sys.argv[1]

    print("Enter your file:")
    path = input()
    add_blank('./archive/' + path)