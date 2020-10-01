#!/usr/bin/python3

import sys, os
from PyPDF2 import PdfFileReader, PdfFileWriter

def add_blank(path):
    path_blank_page = './white_page.pdf'

    blank_page = PdfFileReader(path_blank_page)

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

def pdf_splitter(path):

    for page in range(pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = './temp/{}.pdf'.format(page+1)
        
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            
        #print('Created: {}'.format(output_filename))
    print('Pdf is splitted')


if __name__ == '__main__':

    path = './archive/' + sys.argv[1]

    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pages = pdf.getNumPages()

    print('Pages: ' + str(pages))

    #add_blank(path)
    pdf_splitter(path)