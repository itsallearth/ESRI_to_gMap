import arcpy
import pythonaddins
import webbrowser
from threading import Thread

class ButtonClass1(object):
    """Implementation for ESRI_to_gMap_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		print "Hello"
		try:
			mxd = arcpy.mapping.MapDocument("Current")
            #Check for the active view, add warning if ArcMap is in layout view
			if mxd.activeView=="PAGE_LAYOUT":
				msgbox = pythonaddins.MessageBox("This tool does not work in layout view, please change to active view", "CHANGE TO ACTIVE VIEW", 0)
			else:
				# reference the active dataframe
				dataframe_string = mxd.activeView
				dataframe= arcpy.mapping.ListDataFrames(mxd,dataframe_string)[0]
				crntspatialref = dataframe.spatialReference
                # scale levels (== z = zoomlevels) used by Google Maps, based on estimation...
				externalScales = [591657551, 295828775, 147914388, 73957194, 36978597, 18489298, 9244649, 4622325, 2311162, 1155581, 577791, 288895, 144448, 72224, 36112, 18056, 9028, 4514, 2257, 1128]
                # get the current dataframe's scale
				currentScale = dataframe.scale
				z = 0
                # search for the appropiate zoomlevel for Gmaps
				for scale in externalScales:
					current = int(scale - currentScale)
					if current <= 0 :
						break
                    #counts the zoomlevel
					z=z+1
				x = (dataframe.extent.XMin + dataframe.extent.XMax)/2
				y = (dataframe.extent.YMin + dataframe.extent.YMax)/2

				pt = arcpy.Point()
				pt.X = 6139739.365 #this will be supplied by the dataframe
				pt.Y = 2103989.682 #this will be supplied by the dataframe
				ptgeo = arcpy.PointGeometry(pt, inputSRS)
				ptgeo1 = ptgeo.projectAs(outputSRS)
				pt1 = ptgeo1.lastPoint
				print pt1.X
				print pt1.Y

class ButtonClass2(object):
    """Implementation for ESRI_to_gMap_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass23(object):
    """Implementation for ESRI_to_gMap_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass3(object):
    """Implementation for ESRI_to_gMap_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass4(object):
    """Implementation for ESRI_to_gMap_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass