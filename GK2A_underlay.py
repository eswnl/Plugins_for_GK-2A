#!/usr/bin/env python

# GK-2A animation
# Adds underlay to each layer

from gimpfu import *

def GK2A_underlay(image,drawable,file):
    # function code goes here...
	
	#go to the top layer
	pdb.gimp_image_set_active_layer(image, image.layers[0])
	
	for i in range(len(image.layers)):
		layer = pdb.gimp_file_load_layer(image, file)
		image.add_layer(layer)
		pdb.gimp_image_set_active_layer(image, image.layers[i+1])
		#get layer name
		name = pdb.gimp_item_get_name(pdb.gimp_image_get_active_layer(image))
		pdb.gimp_drawable_levels(pdb.gimp_image_get_active_layer(image), 0, 0.25, 1, FALSE, 1.0, 0, 1, FALSE)
		pdb.gimp_layer_add_alpha(pdb.gimp_image_get_active_layer(image))
		pdb.plug_in_colortoalpha(image, pdb.gimp_image_get_active_layer(image), (30,30, 30))
		pdb.gimp_image_raise_item(image, pdb.gimp_image_get_active_layer(image))
		layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		#set layer name
		pdb.gimp_item_set_name(pdb.gimp_image_get_active_layer(image), name)
		pdb.gimp_drawable_levels(pdb.gimp_image_get_active_layer(image), 0, 0.33, 1, FALSE, 1.0, 0, 1, FALSE)
		if(i < len(image.layers)-1):
			pdb.gimp_image_set_active_layer(image, image.layers[i+1])
	
register(
    "GK-2A_underlay",
    "Adds the GK-2A satellite underlay to each layer for animation",
    "Adds underlay to each layer",
    "John Bell", "John Bell", "2019",
    "Apply underlay to layers for animation",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
		(PF_FILE, "file", "File to open", None)
    ],
    [],
    GK2A_underlay, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()