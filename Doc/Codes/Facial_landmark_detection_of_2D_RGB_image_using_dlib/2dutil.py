# will contain basic utilities for 2D method:

import numpy as np

def plot1:
	# Compute histogram values
	import numpy as np
	histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

	# Save results to a new table node
	tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
	updateTableFromArray(tableNode, histogram)
	tableNode.GetTable().GetColumn(0).SetName("Count")
	tableNode.GetTable().GetColumn(1).SetName("Intensity")

	# Create plot
	plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", volumeNode.GetName() + ' histogram')
	plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
	plotSeriesNode.SetXColumnName("Intensity")
	plotSeriesNode.SetYColumnName("Count")
	plotSeriesNode.SetPlotType(plotSeriesNode.PlotTypeScatterBar)
	plotSeriesNode.SetColor(0, 0.6, 1.0)

	# Create chart and add plot
	plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
	plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())
	plotChartNode.YAxisRangeAutoOff()
	plotChartNode.SetYAxisRange(0, 500000)

	# Show plot in layout
	slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)

def plot2:
	# Get a volume from SampleData and compute its histogram
	import SampleData
	import numpy as np
	volumeNode = SampleData.SampleDataLogic().downloadMRBrainTumor1()
	histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

	chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
	chartNode.SetYAxisRangeAuto(False)
	chartNode.SetYAxisRange(0, 4e5)

def 
