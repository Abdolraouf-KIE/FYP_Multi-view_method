# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2



#adding fiducials by 3D coordinates
slicer.modules.markups.logic().AddFiducial(344, 53, 185) #ras coordinates

#fidning the ras position of pikced point.
        # OPTION1
# displayPosition = [100,120]

# Get model displayable manager
modelDisplayableManager = None
threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
managers = vtk.vtkCollection()
threeDViewWidget.getDisplayableManagers(managers)
for i in range(managers.GetNumberOfItems()):
  obj = managers.GetItemAsObject(i)
  if obj.IsA('vtkMRMLModelDisplayableManager'):
    modelDisplayableManager = obj
    break

# Use model displayable manager's point picker
# pickedPosition = []
# if modelDisplayableManager.Pick(displayPosition[0], displayPosition[1]):
    # rasPositionArray = vtk.vtkDoubleArray()
    # rasPositionArray.SetVoidArray(modelDisplayableManager.GetPickedRAS(),3,1)
    # rasPosition = [rasPositionArray.GetValue(i) for i in range(3)]
        # OPTION2
#This code is to activate the markup placement mode from which the user is expected to click on surface. lets find the second half of the code.
interactionNode = slicer.app.applicationLogic().GetInteractionNode()
selectionNode = slicer.app.applicationLogic().GetSelectionNode()
selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsFiducialNode")
fiducialNode = slicer.vtkMRMLMarkupsFiducialNode()
slicer.mrmlScene.AddNode(fiducialNode)
fiducialNode.CreateDefaultDisplayNodes() 
selectionNode.SetActivePlaceNodeID(fiducialNode.GetID())
interactionNode.SetCurrentInteractionMode(interactionNode.Place)

print(rasPosition)