# Usage:
# make        # make booklet
# make clean  # remove temp

.PHONY: all add_blank_pages split_pdf sort_pages merge_booklet clean

all: add_blank_pages split_pdf  # sort_pages merge_booklet

#.DEFAULT_GOAL := add_blank_pages

add_blank_pages:
	@echo "Adding blank pages..."
	@python3 ./make_booklet/add_blank_pages.py
	

split_pdf:
	@echo "Splitting pdf..."
	@python3 ./make_booklet/split_pdf.py

sort_pages:

merge_booklet:

clean:
	@echo "Cleaning up..."
	rm -fr ./temp
	rm -fr ./new