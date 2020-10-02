#!/usr/bin/python

import sys, shutil, glob, time
from PyPDF2 import PdfFileWriter, PdfFileReader

def merger(input_paths, output_path):

    pdf_writer = PdfFileWriter()

    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

    time.sleep(10)
    shutil.rmtree('./new')

if __name__ == '__main__':
    paths = glob.glob('./new/*.pdf')
    paths.sort()
    merger(paths, './booklets/' + sys.argv[1])