# /home/raouf/Documents/Tools/Slicer-4.11.20200930-linux-amd64/bin/PythonSlicer
#exec(open("/home/raouf/Documents/UM/SEM5/FYP/MLRegistration/Doc/Codes/Facial_landmark_detection_of_2D_RGB_image_using_dlib/Task2_Capture_image.py").read())

import sys
import os

# having the node as variable for manipulation #TODO find a way to automatically load the first model and then load and manipulate the others.
# masterVolumeNode=getNode('3: VOLUMETRIC AXIAL_4')

# center the 3d view
layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()

# Rotate the 3d view
layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
# threeDView.yaw()

# position the camera infront of the face:
view = layoutManager.threeDWidget(0).threeDView() #the zero is the index of the first camera/threeDview
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)
cameraNode.SetPosition(0,500,0)


#capture the scene view
renderWindow = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
writer = vtk.vtkPNGWriter()
writer.SetFileName("/home/raouf/Documents/UM/SEM5/FYP/MLRegistration/Doc/Codes/Facial_landmark_detection_of_2D_RGB_image_using_dlib/Data/imgs/screenshot.png")
writer.SetInputConnection(wti.GetOutputPort())
writer.Write()

