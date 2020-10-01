#!/usr/bin/python

import sys, os
from PyPDF2 import PdfFileReader, PdfFileWriter

def sort_pages(path):
		pdf = PdfFileReader(path)
	    pages = pdf.getNumPages()

        counter = 2

        for page in range(pages):

            pageCorrected = page + 1
            counterCorrected = str(counter).zfill(2)

            input_page = './temp/' + str(pageCorrected) + '.pdf'
			output_page = './new/' + counterCorrected +'.pdf'

            if pageCorrected < (pages / 2):

                if (pageCorrected % 2) == 0:
                    os.rename(input_page,output_page)
                    print(str(pageCorrected) + " is " + counterCorrected)
                    counter = counter + 3

                else:
                    os.rename(input_page, output_page)
                    print(str(pageCorrected) + " is " + counterCorrected)
                    counter = counter + 1

            elif pageCorrected == (pages / 2):
                os.rename(input_page, output_page)
                print(str(pageCorrected) + " is " + counterCorrected)
                counter = counter + 1

            else:
                if (pageCorrected % 2) == 0:
                    os.rename(input_page, output_page)
                    print(str(pageCorrected) + " is " + counterCorrected)
                    counter = counter - 1

                else:
                    os.rename(input_page, output_page)
                    print(str(pageCorrected) + " is " + counterCorrected)
                    counter = counter - 3

if __name__ == '__main__':
    path = sys.argv[1]
    add_blank('./archive/' + path)