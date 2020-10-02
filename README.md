# Toolkit to make booklets
To begin make sure you have installed: 

	makefile, python3, PyPDF2, imageMagick

Clone the repository (or download it):

	git clone 

List usage:

	make help

Initialize folders:

	make init

Now you can move your pdfs into the archive directory!

Generate your booklet into the /booklets folder (remember that the 'nameFile' must be without extension .pdf): 

	make file='nameFile' booklet

Generate your booklet into the /booklets folder from a double-pages pdf (remember that the 'nameFile' must be without extension .pdf): 

	make file='nameFile' single_pages_booklet

You can also generate a single-pages pdf into the /archive folder from double-pages pdf (remember that the 'nameFile' must be without extension .pdf): 

	make file='nameFile' single_pages

If you get stuck, remember to clean the temporary folders before to start again:

	make clean


# Other tools

get number of pages

	pdftk my.pdf dump_data | grep NumberOfPages | sed 's/[^0-9]*//'

select a part of a pdf (first part/ second part / jump a page)

    pdftk foo-bar.pdf cat 1-12 output foo.pdf

    pdftk foo-bar.pdf cat 13-end output bar.pdf

    pdftk in.pdf cat 1-12 14-end output out.pdf

convert pdf to images

	convert -density 300 foo-bar.pdf bar%02d.jpg

crop image in 2

	convert bar*.jpg -gravity East -crop 50%x100%+0+0 ./right/right%02d.jpg

	convert bar*.jpg -gravity West -crop 50%x100%+0+0 ./left/left%02d.jpg

rename left & right

	python3 rename.py

convert images to pdf

	convert *.jpg paper.pdfs