# GIMP Plugins for GK-2A
Apply overlays and underlays automatically to GK-2A IR images in GIMP.

GK-2A created by the KMA Meterological Organisation is a geostationary satellite transmitting both LRIT and HRIT. The aim of these plugins is to automatically add overlays and underlays to the (now only available) monochrome IR images when they are opened as layers. To use these plug-ins require the host software GIMP editor to be installed. 

Once the layers have been processed, use GIMP animation feature to create your animation.

## Options
Plugin | In GIMP | Input |
------------ | ------------- | ------------- |
GK2A_Date and Time.py | Apply date and time to layers for animation | None 
GK2A_Auto_Adjust.py | auto adjust layers for animation | None
GK2A_enhancement_overlay.py | Apply IR enhancement to layers for animation | None
GK2A_overlay.py | Apply overlay to layers for animation | Path to overlay file (.gif) - see folder for samples
GK2A_underlay.py | Apply underlay to layers for animation | Path to underlay file (bitmap image) - see folder for samples

## Adding date and time
This plug-in extracts the time information from the file name and stamps it on the image/layer. Open all the IR images as layers (select "Open as layers" from the File menu)

![Time Stamp](SampleImages/TestTimeStamp.gif)

## Auto adjust - Tries to emphasize the land
This plug-in increases contrast between land and sea.

![AutoAdjustTest](SampleImages/AutoAdjustTest.png)
## Applying the GK-2A IR enhancement overlay
Using the IR enhancement tool developed by Sam (https://github.com/sam210723/xrit-rx), you can create the corresponding IR enhancement for the IR image. Make sure you set the option to transparent when creating the IR enhancement images and allow it to generate all the IR enhancement for every image in your output folder.

The command to run:
```
python enhance-ir.py "Folder" -t
```
Then your folder should contain the enhancement files.
![EnhancementImages](SampleImages/ShowingEnhancementFiles.png)

In GIMP, open just the IR jpeg images as layers. Use the filter to just show jpeg files (it will be easier to select just the jpg)

By selecting the "Apply IR enhancement to layers for animation", the plugin will apply all the IR enhancement png transparencies on all the layers. The plugin will automatically search the current folder for the png transparencies that you created.

![EnhancementImageAnimation](SampleImages/Animation3.gif)

## Applying overlays

Applies overlay such as longitude/latitude grid/outline maps to each layer. It will ask you the overlay gif file to use.

![OverlayTest](SampleImages/overlayTest.png)


## Applying underlays

Create artificial colour maps to apply land and sea colours. It will ask you the underlay bitmap file to use. 
You can create own bitmaps as well.

![UnderlayTest](SampleImages/UnderlayTest.png)

Animation of Hagibis.

![OverlayAnimationTest](SampleImages/Hagibis.gif)

## Installation

Copy the plugin files (the .py files) to the GIMP plugin directory. For my copy of GIMP, it is:
```
GIMP 2\lib\gimp\2.0\plug-ins
```

If successful, the GK-2A menus should appear in the GIMP's Layer menu
![GK-2A menus](SampleImages/GK-2Amenus2.png)
