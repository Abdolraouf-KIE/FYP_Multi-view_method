# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2



#fidning the ras position of pikced point.
        # OPTION1
# the display positions of the landmarks obtained from Task4 are placed here. For testing purpose we set an arbitary point.
displayPosition = [0,0]

count=0

# Get model displayable manager
modelDisplayableManager = None
threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
managers = vtk.vtkCollection()      # the manager contains the MRMLModelDisplayavleManager among other things. So we need to select the desired node.
threeDViewWidget.getDisplayableManagers(managers)
for i in range(managers.GetNumberOfItems()):
  obj = managers.GetItemAsObject(i)
  count=count+1
  if obj.IsA('vtkMRMLModelDisplayableManager'):
    modelDisplayableManager = obj
    print(count)
    break

# Use model displayable manager's point picker
pickedPosition = []
if modelDisplayableManager.Pick(displayPosition[0], displayPosition[1]):
    rasPositionArray = vtk.vtkDoubleArray()
    rasPositionArray.SetVoidArray(modelDisplayableManager.GetPickedRAS(),3,1)
    rasPosition = [rasPositionArray.GetValue(i) for i in range(3)]

print(rasPosition) # ras position is the coordiante system used by 3d Slicer.


        # OPTION2 for using point picker.
#This code is to activate the markup placement mode from which the user is expected to click on surface. lets find the second half of the code.
# interactionNode = slicer.app.applicationLogic().GetInteractionNode()
# selectionNode = slicer.app.applicationLogic().GetSelectionNode()
# selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsFiducialNode")
# fiducialNode = slicer.vtkMRMLMarkupsFiducialNode()
# slicer.mrmlScene.AddNode(fiducialNode)
# fiducialNode.CreateDefaultDisplayNodes() 
# selectionNode.SetActivePlaceNodeID(fiducialNode.GetID())
# interactionNode.SetCurrentInteractionMode(interactionNode.Place)

#adding fiducials by 3D coordinates
slicer.modules.markups.logic().AddFiducial(rasPosition[0], rasPosition[1], rasPosition[2]) #ras coordinates

#OPTION3:   alternative means of using markup nodes:
markupsNode = slicer.mrmlScene.GetFirstNodeByName('F')
if not markupsNode:
  markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode","F")

if markupsNode.GetNumberOfFiducials() == 0:
    markupsNode.AddFiducial(*ras)

# OPTION4:(BEST) This should help in fixing the picking function: 
# hhttps://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationDisplayableManager.cxx
# The mouse is used to obtain the ras coordinates. The library above handels such a thing and it uses modeldisplayablemanager
# The annotation module has two functions: GetDisplayToWorldCoordinates() and OnClickInRenderWindowGetCoordinates (). both manipulate the y value with respect to the window height

{References:
Main picker library: (several suitbale functions such as vtk pickers as well as Pick() function)
https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLModelDisplayableManager.cxx

Another node that makes use of the library:
https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationDisplayableManager.cxx 

Discourse 3DSlicer (fiducial projection):
https://discourse.slicer.org/t/how-to-create-a-fiducial-though-the-pixel-not-the-mouse-event/11410/2
}