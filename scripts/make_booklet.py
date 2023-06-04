#!/usr/bin/python3

import sys, os, shutil, glob, time
from PyPDF2 import PdfReader, PdfWriter


def add_blank(path, pages):
    path_blank_page = './white_page.pdf'

    blank_page = PdfReader(path_blank_page)
    os.mkdir('temp')
    if (pages%4) == 0:
        print('Pages are already a multiple of 4')
       #os.mkdir('temp')

        return pages

    else:
        print('Adding missing pages...')

        #os.mkdir('temp')
        while True:
            missing = pages%4
            pages = pages + 1
            
            pdf_writer = PdfWriter()
            pdf_writer.add_page(blank_page.pages[0])
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

    pages = len(pdf.pages)

    for page in range(pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page])
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

    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

    # time.sleep(10)
    shutil.rmtree('new')

    print('Booklet ready to print!')



if __name__ == '__main__':
    input_path = './archive/' + sys.argv[1]
    output_path = './booklets/' + sys.argv[1]

    fname = os.path.splitext(os.path.basename(input_path))[0]

    pdf = PdfReader(input_path)
    pages = len(pdf.pages)
    
    print('Starting pages: ' + str(pages))

    #add_blank(path, pages)
    total_pages = add_blank(input_path, pages)   # this run the function and save the returned value
    pdf_splitter(input_path, pages)
    sort_pages(total_pages)
    merger(output_path)
