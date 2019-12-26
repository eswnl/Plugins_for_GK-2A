#!/usr/bin/env python

# GK-2A animation
# Auto adjust each layer

from gimpfu import *

def GK2A_Auto_Adjust(image,drawable):
	# function code goes here...

	#go to the top layer
	pdb.gimp_image_set_active_layer(image, image.layers[0])
    
	for i in range(len(image.layers)):
		
		pdb.gimp_image_set_active_layer(image, image.layers[i])
		pdb.gimp_drawable_levels(pdb.gimp_image_get_active_layer(image), 0, 0.25, 1, FALSE, 1.0, 0, 1, FALSE)
		
		if(i < len(image.layers)):
			pdb.gimp_image_set_active_layer(image, image.layers[i+1])
	
	
register(
    "GK-2A_Auto_Adjust",
    "Auto adjust layer for animation",
    "Auto adjust each layer",
    "John Bell", "John Bell", "2019",
    "Auto adjust layers for animation",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
    ],
    [],
    GK2A_Auto_Adjust, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()