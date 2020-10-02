#!/usr/bin/python3

import sys, os, shutil, glob, time
from PyPDF2 import PdfFileReader, PdfFileWriter


def add_blank(path, pages):
    path_blank_page = './white_page.pdf'

    blank_page = PdfFileReader(path_blank_page)

    if (pages%4) == 0:
        print('Pages are already a multiple of 4')

        return pages

    else:
        print('Adding missing pages...')

        os.mkdir('temp')
        while True:
            missing = pages%4
            pages = pages + 1
            
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(blank_page.getPage(0))
            output_filename = './temp/{}.pdf'.format(pages)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            #print('Add blank page: {}'.format(output_filename))

            if (pages%4) == 0:
                break
        print('done')

        return pages


def pdf_splitter(path, pages):
    print('Splitting pdf...')

    pages = pdf.getNumPages()

    for page in range(pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = './temp/{}.pdf'.format(page+1)
        
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            
        #print('Created: {}'.format(output_filename))
    print('done')


def sort_pages(total_pages):
    print('Rearranging pages...')

    counter = 2

    os.mkdir('new')

    for page in range(total_pages):

        pageCorrected = page + 1

        input_page = './temp/' + str(pageCorrected) + '.pdf'
        output_page = './new/' + str(counter).zfill(2) +'.pdf'

        if pageCorrected < (total_pages/2):

            if (pageCorrected % 2) == 0:
                os.rename(input_page, output_page)
                #print(str(pageCorrected) + " is " + str(counter).zfill(2))
                counter = counter + 3
            else:
                os.rename(input_page, output_page)
                #print(str(pageCorrected) + " is " + str(counter).zfill(2))
                counter = counter + 1

        elif pageCorrected == (total_pages/2):
            os.rename(input_page, output_page)
            #print(str(pageCorrected) + " is " + str(counter).zfill(2))
            counter = counter + 1

        else:

            if (pageCorrected % 2) == 0:
                os.rename(input_page, output_page)
                #print(str(pageCorrected) + " is " + str(counter).zfill(2))
                counter = counter - 1
            else:
                os.rename(input_page, output_page)
                #print(str(pageCorrected) + " is " + str(counter).zfill(2))
                counter = counter - 3

    shutil.rmtree('temp')

    print('done')


def merger(output_path):
    print('Mergin booklet...')

    paths = glob.glob('./new/*.pdf')
    paths.sort()

    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

    # time.sleep(10)
    shutil.rmtree('new')

    print('Booklet ready to print!')



if __name__ == '__main__':
    input_path = './archive/' + sys.argv[1]
    output_path = './booklets/' + sys.argv[1]

    fname = os.path.splitext(os.path.basename(input_path))[0]

    pdf = PdfFileReader(input_path)
    pages = pdf.getNumPages()
    
    print('Starting pages: ' + str(pages))

    #add_blank(path, pages)
    total_pages = add_blank(input_path, pages)   # this run the function and save the returned value
    pdf_splitter(input_path, pages)
    sort_pages(total_pages)
    merger(output_path)