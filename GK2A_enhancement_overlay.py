#!/usr/bin/env python

# GK-2A animation
# Adds enhancement overlay to each layer

from gimpfu import *

def GK2A_enhancement_overlay(image,drawable):
    # function code goes here...
	
	#go to the top layer
	pdb.gimp_image_set_active_layer(image, image.layers[0])
	
	
	
	path_name = pdb.gimp_image_get_filename(image)[:-36]
	pdb.gimp_message("Searching "+path_name+ "for enhancement overlays")
	for i in range(len(image.layers)):
			
		layer = pdb.gimp_file_load_layer(image, path_name+(pdb.gimp_item_get_name(pdb.gimp_image_get_active_layer(image))[:-4]+"_ENHANCED.png"))
		image.add_layer(layer)
		layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		if(i < len(image.layers)-1):
			pdb.gimp_image_set_active_layer(image, image.layers[i+1])
	
register(
    "GK-2A_enhancement_overlay",
    "Adds the IR enhancement overlay to each layer for animation",
    "Adds IR overlay to each layer",
    "John Bell", "John Bell", "2019",
    "Apply IR enhancement overlay to layers for animation",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
    ],
    [],
    GK2A_enhancement_overlay, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()