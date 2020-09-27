# Toolkit to make booklets
run

	python3 split.py

and then

	python3 merge.py

# Other tools

get number of pages

	pdftk my.pdf dump_data | grep NumberOfPages | sed 's/[^0-9]*//'

select a part of a pdf (first part/ second part / jump a page)

    pdftk foo-bar.pdf cat 1-12 output foo.pdf

    pdftk foo-bar.pdf cat 13-end output bar.pdf

    pdftk in.pdf cat 1-12 14-end output out.pdf

convert to images

	convert -density 300 foo-bar.pdf bar%02d.jpg

crop image in 2

	convert bar*.jpg -gravity East -crop 52%x100%+0+0 ./right/right%02d.jpg

	convert bar*.jpg -gravity West -crop 49%x100%+0+0 ./left/left%02d.jpg

rename left & right

	python3 rename.py