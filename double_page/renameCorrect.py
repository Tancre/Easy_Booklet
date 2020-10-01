#!/usr/bin/python

import sys
from os import listdir, rename

def rename_even(path):

	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/' + path +'/right'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = 'bifo-{:02}.jpg'.format(oldNumber*2+1)
	    # This will rename the old file.

	    rename('./archive/' + path +'/right/'+ filename,'./archive/' + path +'/finished/'+ newName)

def rename_odd(path):

	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/' + d_input +'/left'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = d_input +'-{:02}.jpg'.format(oldNumber*2)
	    # This will rename the old file.

	    rename('./archive/' + d_input +'/left/'+filename,'./archive/' + d_input +'/finished/'+newName)



if __name__ == '__main__':
    path = sys.argv[1]
	rename_even(path)
	rename_odd(path)