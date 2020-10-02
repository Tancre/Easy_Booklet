#!/usr/bin/python

import sys
from shutil import copyfile
from os import listdir, rename, mkdir

def rename_even(path):

	# This will loop over all the filenames in the current directory:
	for filename in listdir(path +'/right'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = '{:02}.jpg'.format(oldNumber*2+1)
	    # This will rename the old file.

	    copyfile(path +'/right/'+ filename,path +'/finished/'+ newName)

def rename_odd(path):

	# This will loop over all the filenames in the current directory:
	for filename in listdir(path +'/left'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = '{:02}.jpg'.format(oldNumber*2)
	    # This will rename the old file.

	    copyfile(path +'/left/'+filename, path +'/finished/'+newName)



if __name__ == '__main__':
	path = './temp' # + sys.argv[1]

	rename_even(path)
	rename_odd(path)