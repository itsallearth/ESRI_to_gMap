# ESRI to Google Maps

ESRI to Google Maps is an ArcMap AddIn.  This particular addin is written in Python and ArcPy.  It is designed to make the switch as quick and easy as aspossible. Switch form the map extent you are working form in ArcMap to the same extent of the in Google Maps. It's a one click action... Fast, clean and simple. 

## Description
Included in the ESRI_to_gMap.addin file

## Installation
Copy the ESRI_to_gMap.addin somewhere on your computer and double click it.  This will add the addin to ArcMap.  You will see the toolbar when you click customize > toolbars: 

![alt text](http://itsallearth.com/images/ESRItoGM.png "ESRI toolbar diagram").


The toolbar will look loike this: ![alt text](http://itsallearth.com/images/toolbar.JPG "ESRI toolbar").

Each button (except for the Google Search button) uses this function to capture the extent of the map and the center point in ArcMap:

```def centerPoint():
	mxd = arcpy.mapping.MapDocument("CURRENT")
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	inputSRS = df.spatialReference
	#inputSRS = arcpy.SpatialReference(2230)
	outputSRS = arcpy.SpatialReference(4236)
	mxd = arcpy.mapping.MapDocument("Current")
	if mxd.activeView == "PAGE_LAYOUT":
		msgbox = pythonaddins.MessageBox("This tool does not work in layout view, please change to active view", "CHANGE TO ACTIVE VIEW", 0)
	else:
		df_str = mxd.activeView
		dataframe= arcpy.mapping.ListDataFrames(mxd, df_str)[0]
		crntspatialref = dataframe.spatialReference
		#scale levels (== z = zoomlevels) used by Google Maps, based on estimation...
		externalScales = [591657551, 295828775, 147914388, 73957194, 36978597, 18489298, 9244649, 4622325, 2311162, 1155581, 577791, 288895, 144448, 72224, 36112, 18056, 9028, 4514, 2257, 1128]
		Meters = [35131070, 17565535, 8782767, 4391384, 2195692, 1097846, 548923, 274461, 137231, 68615, 34308, 17154, 8577, 4288, 2144, 1072, 536, 268, 134, 67]
		currentScale = dataframe.scale #get the current dataframe's scale
		z = 0
		metersl = 0
		# search for the appropiate zoomlevel for Gmaps
		for scale in externalScales:
			current = int(scale - currentScale)
			if current <= 0 :
				break
			z=z+1 #counts the zoomlevel
			metersl = Meters[z]

		print "Meters: "+ str(metersl)
		xx = (dataframe.extent.XMin + dataframe.extent.XMax)/2 
		yy = (dataframe.extent.YMin + dataframe.extent.YMax)/2

		x_min = dataframe.extent.XMin
		y_min = dataframe.extent.YMin

		print "Lower xy:"
		print str(y_min) + ": Y"
		print str(xx) + ": X"
		
		print xx
		print yy
		print ""
		
		pt = arcpy.Point()
		
		#pt.X2 = x_min
		pt3 = arcpy.Point()

		pt3.X = xx
		pt3.Y = y_min
		ptgeo = arcpy.PointGeometry(pt3, inputSRS)
		ptgeo3 = ptgeo.projectAs(outputSRS)
		pt13 = ptgeo3.lastPoint
		print "newX : "+str(pt13.X)
		print "newY : "+str(pt13.Y)
		print z
		
		
		pt.X = xx #xx supplied by the dataframe
		pt.Y = yy #yy supplied by the dataframe
		ptgeo = arcpy.PointGeometry(pt, inputSRS)
		ptgeo1 = ptgeo.projectAs(outputSRS)
		pt1 = ptgeo1.lastPoint
		print pt1.X
		print pt1.Y
		print z

		return [pt1.X, pt1.Y, z, pt13.Y, metersl]
		#return [pt1.X, pt1.Y, z, pt13.X]```

```
## Usage Instructions
This is where you lay out all the commands available or how you make your software do its magic. This can be CLI, REST, powershell commands, etc. Remember to use the backtick characters to highlight code `such as this` or create sections of code using three backticks in a row

## Future
Look for more tools for this addin in the near future.


