#!/usr/bin/python

import sys, os, glob, shutil, time
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_add_blank(path, paths):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pages = pdf.getNumPages()

    missing_pages = pages%4
    os.mkdir('./temp')
    total_pages = add_blank(path, pages, fname)

    add_blank(path, pages, fname)
    pdf_splitter(path, pdf, pages, fname)

    rename(total_pages)
    merger(sys.argv[2], paths, total_pages)

    shutil.rmtree('./temp')
    # time.sleep(10)
    # shutil.rmtree('./new')


def add_blank(path, pages, fname):
    path_blank_page = './white_page.pdf'
    pdf = PdfFileReader(path_blank_page)

    if (pages%4) == 0:
        print('True')
    else:
        while True:
            print('initial pages: ' + str(pages))
            missing = pages%4
            pages = pages + 1
            
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(0))
            output_filename = './temp/{}.pdf'.format(pages)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            print('add blank page: {}'.format(output_filename))

            if (pages%4) == 0:
                break
        print(pages)
        return pages

def pdf_splitter(path, pdf, pages, fname):
    for page in range(pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = './temp/{}.pdf'.format(page+1)
        
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            
        #print('Created: {}'.format(output_filename))
    print('base')

def rename(total_pages):
        counter = 2

        for page in range(total_pages):
            pageCorrected = page + 1
            if pageCorrected < (total_pages/2):
                if (pageCorrected % 2) == 0:
                    os.rename('./temp/' + str(pageCorrected) + '.pdf', './new/' +  str(counter).zfill(2) +'.pdf')
                    print(str(pageCorrected) + " is " + str(counter).zfill(2))
                    counter = counter + 3
                else:
                    os.rename('./temp/' + str(pageCorrected) + '.pdf', './new/' +  str(counter).zfill(2) +'.pdf')
                    print(str(pageCorrected) + " is " + str(counter).zfill(2))
                    counter = counter + 1
            elif pageCorrected == (total_pages/2):
                os.rename('./temp/' + str(pageCorrected) + '.pdf', './new/' +  str(counter).zfill(2) +'.pdf')
                print(str(pageCorrected) + " is " + str(counter).zfill(2))
                counter = counter + 1
            else:
                if (pageCorrected % 2) == 0:
                    os.rename('./temp/' + str(pageCorrected) + '.pdf', './new/' +  str(counter).zfill(2) +'.pdf')
                    print(str(pageCorrected) + " is " + str(counter).zfill(2))
                    counter = counter - 1
                else:
                    os.rename('./temp/' + str(pageCorrected) + '.pdf', './new/' +  str(counter).zfill(2) +'.pdf')
                    print(str(pageCorrected) + " is " + str(counter).zfill(2))
                    counter = counter - 3

def merger(output_path, input_paths, total_pages):

    pdf_writer = PdfFileWriter()

    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    path = sys.argv[1]
    paths = glob.glob('./new/*.pdf')
    paths.sort()
    split_add_blank(path, paths)
