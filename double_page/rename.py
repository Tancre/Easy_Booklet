import sys
from os import listdir, rename

d_input = sys.argv[1]

def rename_even(d_input):
	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/' + d_input +'/right'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = 'bifo-{:02}.jpg'.format(oldNumber*2+1)
	    # This will rename the old file.

	    rename('./archive/' + d_input +'/right/'+ filename,'./archive/' + d_input +'/finished/'+ newName)

def rename_odd(arg2):
	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/' + d_input +'/left'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = d_input +'-{:02}.jpg'.format(oldNumber*2)
	    # This will rename the old file.

	    rename('./archive/' + d_input +'/left/'+filename,'./archive/' + d_input +'/finished/'+newName)


rename_even(d_input)
rename_odd(d_input)