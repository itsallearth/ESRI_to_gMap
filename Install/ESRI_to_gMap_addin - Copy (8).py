import arcpy
import pythonaddins
import webbrowser
from threading import Thread

def centerPoint():
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
		currentScale = dataframe.scale #get the current dataframe's scale
		z = 0
		# search for the appropiate zoomlevel for Gmaps
		for scale in externalScales:
			current = int(scale - currentScale)
			if current <= 0 :
				break
			z=z+1 #counts the zoomlevel
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

		return [pt1.X, pt1.Y, z, pt13.Y]
		#return [pt1.X, pt1.Y, z, pt13.X]

class ButtonClass1(object):
    """Implementation for ESRI_to_gMap_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#View current extent in satellite
		values = centerPoint()
		print values[0]
		print values[1]
		print values[2]

		link = "https://www.google.com/maps/@?api=1&map_action=map&center=" + str(values[1]) + "," + str(values[0]) + "&zoom=" + str(values[2])+"&basemap=satellite"
		print link

		arcpy.AddMessage(link + '\n')
		def OpenBrowserURL():
			webbrowser.open(link,new=2)
		
		t = Thread(target=OpenBrowserURL)
		t.start()
		t.join()		
		
class ButtonClass2(object):
    """Implementation for ESRI_to_gMap_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#3D
		values = centerPoint()
		link = "https://www.google.com/maps/@"+str(values[3]) + "," + str(values[0])+",341a,35y,7.31h,72.14t/data=!3m1!1e3"

		arcpy.AddMessage(link + '\n')
		def OpenBrowserURL():
			webbrowser.open(link,new=2)
		
		t = Thread(target=OpenBrowserURL)
		t.start()
		t.join()

class ButtonClass23(object):
    """Implementation for ESRI_to_gMap_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#Google mark
		link = "https://www.google.com" #opens a new google search box
		def OpenBrowserURL():
			webbrowser.open(link,new=2)		
		t = Thread(target=OpenBrowserURL)
		t.start()
		t.join()

class ButtonClass3(object):
    """Implementation for ESRI_to_gMap_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#Bike travelmode=bicycling
		values = centerPoint()
		link = "https://www.google.com/maps/@?api=1&map_action=map&center=" + str(values[1]) + "," + str(values[0]) + "&zoom=" + str(values[2])+"&basemap=roadmap&layer=transit&travelmode=bicycling"
		arcpy.AddMessage(link + '\n')
		def OpenBrowserURL():
			webbrowser.open(link,new=2)
		
		t = Thread(target=OpenBrowserURL)
		t.start()
		t.join()

class ButtonClass4(object):
    """Implementation for ESRI_to_gMap_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#Traffic basemap=satellite&layer=transit
		values = centerPoint()
		link = "https://www.google.com/maps/@?api=1&map_action=map&center=" + str(values[1]) + "," + str(values[0]) + "&zoom=" + str(values[2])+"&basemap=roadmap&layer=traffic"
		arcpy.AddMessage(link + '\n')
		def OpenBrowserURL():
			webbrowser.open(link,new=2)
		
		t = Thread(target=OpenBrowserURL)
		t.start()
		t.join()
