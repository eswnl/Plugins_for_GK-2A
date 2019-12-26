#!/usr/bin/env python

# GK-2A animation
# Adds overlay to each layer

from gimpfu import *

def GK2A_overlay(image,drawable,file):
    # function code goes here...
	
	#go to the top layer
	pdb.gimp_image_set_active_layer(image, image.layers[0])
	
	for i in range(len(image.layers)):
		
		layer = pdb.gimp_file_load_layer(image, file)
		image.add_layer(layer)
		layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		if(i < len(image.layers)-1):
			pdb.gimp_image_set_active_layer(image, image.layers[i+1])
	
register(
    "GK-2A_overlay",
    "Adds the GK-2A satellite overlay to each layer for animation",
    "Adds overlay to each layer",
    "John Bell", "John Bell", "2019",
    "Apply overlay to layers for animation",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
		(PF_FILE, "file", "File to open", None)
    ],
    [],
    GK2A_overlay, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()