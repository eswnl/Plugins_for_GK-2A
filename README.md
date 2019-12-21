# GIMP Plugins for GK-2A
Apply overlays and underlays automatically to GK-2A IR images in GIMP.

GK-2A created by the KMA Meterological Organisation is a geostationary satellite transmitting both LRIT and HRIT. The aim of these plugins is to automatically add overlays and underlays to the (now only available) monochrome IR images when they are opened as layers. To use these plug-ins require the host software GIMP editor to be installed. 

## Options
Option | Effect
------------ | -------------
GK2A_Date and Time.py | Adds the time and date to each layer
GK2A_Auto_Adjust.py | Automatic contrast correction on each layer
GK2A_enhancement_overlay.py | After generating the IR enhancement images, add to each layer.
GK2A_overlay.py | Add overlay eg. grid, long/lat lines to each layer
GK2A_underlay.py | Insert land and sea colours

## Adding date and time
This plug-in extracts the time information from the file name and stamps it on the image/layer.
![Time Stamp](TimeStamp.png)
