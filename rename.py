from os import listdir, renamecd

def rename_even():
	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/bifo_anatomy_autonomy/right'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = 'bifo-{:02}.jpg'.format(oldNumber*2+1)
	    # This will rename the old file.

	    rename('./archive/bifo_anatomy_autonomy/right/'+ filename,'./archive/bifo_anatomy_autonomy/finished/'+ newName)

def rename_odd():
	# This will loop over all the filenames in the current directory:
	for filename in listdir('./archive/bifo_anatomy_autonomy/left'):
	    # This will cut off the .txt from the end then convert from a string to a number.
	    oldNumber = int(filename[-6:-4])
	    # This line will generate the new filename.
	    newName = 'bifo-{:02}.jpg'.format(oldNumber*2)
	    # This will rename the old file.

	    rename('./archive/bifo_anatomy_autonomy/left/'+filename,'./archive/bifo_anatomy_autonomy/finished/'+newName)


rename_even()
rename_odd()