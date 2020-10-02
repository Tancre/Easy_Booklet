# Usage:!!! the name of 'yourfile' must be without extension .pdf !!!

# make init                                  # creates /archive and /booklets

# make file='yourfile' booklet               # creates booklet 
# make file='yourfile' single_pages          # creates a pdf with single pages
# make file='yourfile' single_pages_booklet  # creates a booklet from a double pages pdf

# make clean                                 # remove temporary folders

.PHONY: all pdf_to_images crop_images rename_images merge_pdf booklet_from_single_page single_page single_page_booklet booklet init help clean

.DEFAULT_GOAL := booklet

# all: pdf_to_images crop_images rename_images merge_pdf # make_booklet

# MAIN TASKS
help:
	@echo ""
	@echo "Usage:"
	@echo ""
	@echo "make help \t\t\t\t\t\t\t show usage"
	@echo "make init \t\t\t\t\t\t\t creates /archive and /booklets"
	@echo "make clean \t\t\t\t\t\t\t remove temporary folders"
	@echo ""
	@echo "make file='fileName(without .pdf)' booklet \t\t\t creates booklet pdf "
	@echo "make file='fileName(without .pdf)' single_pages \t\t creates a pdf with single pages from a double pages pdf"
	@echo "make file='fileName(without .pdf)' single_pages_booklet \t creates a booklet pdf from a double pages pdf"
	@echo ""


init:
	@echo "Easy_Booklet is initialising..."
	@mkdir archive
	@mkdir booklets
	@echo "done"
	@echo "Now you can move your pdfs into the /archive folder"

booklet:
	@echo "The Booklet is creating..."
	@python3 ./scripts/make_booklet.py $(file).pdf

single_page: pdf_to_images crop_images rename_images merge_pdf
single_page_booklet: single_page booklet_from_single_page

clean:
	@echo "Cleaning up..."
	rm -fr ./temp
	rm -fr ./new

# SUBTASKS SINGLE PAGE
pdf_to_images:
	@echo "Converting pdf to images..."
	@mkdir temp
	@convert -density 300 ./archive/$(file).pdf ./temp/$(file)%02d.jpg
	@echo "done"

crop_images:
	@echo "Cropping images at 50% of their width..."
	@mkdir temp/right
	@mkdir temp/left
	@convert ./temp/*.jpg -gravity East -crop 50%x100%+0+0 ./temp/right/right%02d.jpg
	@convert ./temp/*.jpg -gravity West -crop 50%x100%+0+0 ./temp/left/left%02d.jpg
	@echo "done"

rename_images:
	@echo "Reorganise cropped images..."
	@mkdir temp/finished
	@python3 ./scripts/double_page/rename.py $(file).pdf
	@echo "done"

merge_pdf:
	@echo "Converting cropped and reorganised images to pdf..."
	@convert ./temp/finished/*.jpg ./archive/$(file)-single_page.pdf
	@echo "Pdf ready"

booklet_from_single_page:
	@echo "The Booklet is creating..."
	@python3 ./scripts/make_booklet.py $(file)-single_page.pdf