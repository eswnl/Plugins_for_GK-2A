#!/usr/bin/env python

# GK-2A animation
# Adds overlay to each layer

from gimpfu import *

def GK2A_Date_and_time(image,drawable):
    # function code goes here...

	#go to the top layer
	pdb.gimp_image_set_active_layer(image, image.layers[0])
	#generate times
	timelist = ["00:04","00:14","00:24","00:34","00:44", "00:54", "01:04", "01:14", "01:24","01:34", "01:44", "01:54", "02:04", "02:14", "02:24", "02:34", "02:44", "02:54", "03:04", "03:14", "03:24", "03:34", "03:44", "03:54", "04:04", "04:14", "04:24", "04:34", "04:44", "04:54", "05:04", "05:14", "05:24", "05:34","05:44","05:54","06:04", "06:14", "06:24", "06:34", "06:44", "06:54", "07:04", "07:14", "07:24", "07:34", "07:44", "07:54","08:04","08:14","08:24","08:34","08:44","08:54","09:04","09:14","09:24","09:34","09:44","09:54","10:04","10:14","10:24","10:34","10:44","10:54","11:04","11:14","11:24","11:34","11:44","11:54","12:04","12:14","12:24","12:34","12:44","12:54","13:04","13:14","13:24","13:34","13:44","13:54","14:04","14:14","14:24","14:34","14:44","14:54","15:04","15:14","15:24","15:34","15:44","15:54","16:04","16:14","16:24","16:34","16:44","16:54","17:04","17:14","17:24","17:34","17:44","17:54","18:04","18:14","18:24","18:34","18:44","18:54","19:19","19:14","19:24","19:34","19:44","19:54","20:04","20:14","20:24","20:34","20:44","20:54","21:04","21:14","21:24","21:34","21:44","21:54","22:04","22:14","22:24","22:35","22:45","22:55","23:05","23:15","23:25","23:35","23:45","23:55"]

	for i in range(len(image.layers)):
		name = pdb.gimp_item_get_name(pdb.gimp_image_get_active_layer(image)) #get name of thermal layer
		Getdate = name[17:-11]
		Getdate = Getdate[:4] + '-' + Getdate[4:] #insert separator 1
		Getdate = Getdate[:7] + '-' + Getdate[7:] #insert separator 2
		GetTimeIndex = int(name[7:-26])
		UTCtime = timelist[GetTimeIndex]
		
		pdb.gimp_context_set_foreground((255,255,255)) #set text colour
		pdb.gimp_context_set_background((0,0,0)) #set text background colour
		layer = pdb.gimp_layer_new(image, 2200, 2200, 0, "text", 100,0 )
		image.add_layer(layer)
		pdb.gimp_layer_add_alpha(pdb.gimp_image_get_active_layer(image))
		pdb.plug_in_colortoalpha(image, pdb.gimp_image_get_active_layer(image), (0,0,0))
		pdb.gimp_image_select_rectangle(image, 0, 0, 0, 700, 40)
		pdb.gimp_edit_bucket_fill(pdb.gimp_image_get_active_layer(image), 1, 0, 100, 0, FALSE,0,0)
		layer = pdb.gimp_text_layer_new(image, "GK-2A LRIT IR105 "+Getdate+" "+UTCtime+ " UTC", "Courier New", 30, 0)
		image.add_layer(layer)
		layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		layer = pdb.gimp_image_merge_down(image, image.layers[i], 0)
		pdb.gimp_selection_none(image)
		if(i < len(image.layers)):
			pdb.gimp_image_set_active_layer(image, image.layers[i+1])
		
register(
    "GK2A_Date_and_time",
    "Adds the date and time to each layer for animation",
    "Adds the date and time to each layer",
    "John Bell", "John Bell", "2019",
    "Apply date and time to layers for animation",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
		#(PF_FILE, "file", "File to open", None)
    ],
    [],
    GK2A_Date_and_time, menu="<Image>/Layer/GK-2A..")  # second item is menu location

main()