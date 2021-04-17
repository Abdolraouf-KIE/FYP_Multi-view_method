# location of Python Slicer interpreter:    /home/raouf/Documents/Tools/Slicer-4.11.20200930-linux-amd64/bin/PythonSlicer
#To execute this script copy the code below into 3D Slicer python interpreter: (replace the address with absolute path of the script you want to run)
# exec(open("/home/raouf/Documents/UM/SEM5/FYP/MLRegistration/Doc/Codes/Facial_landmark_detection_of_2D_RGB_image_using_dlib/Task2_Capture_image.py").read())
import sys
import os

def skinSeg(masterVolumeNode):
    # Create segmentation
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes () # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)


    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")

    # display()

    # Create segment editor to get access to effects
    print("Create segment editor to get access to effects")
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

    segmentEditorNode.SetSelectedSegmentID(addedSegmentID) #This is important to highlight the desired segment to alter.

    # Thresholding
    print("Thresholding")
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold","99") #different machines have give different intensity values. so the range must be adjusted accordingly.
    effect.setParameter("MaximumThreshold","1534")
    effect.self().onApply()
    # display()

    # Find largest object, remove all other regions from the segment
    slicer.app.processEvents()
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameterDefault("Operation", "KEEP_LARGEST_ISLAND")
    effect.self().onApply()

    # Smoothing
    print("Smoothing")
    segmentEditorWidget.setActiveEffectByName("Smoothing") 
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "MEDIAN")
    effect.setParameter ("KernelSizeMm", 3)
    effect.self().onApply()
    # display()

    # Make segmentation results visible in 3D
    segmentationNode.CreateClosedSurfaceRepresentation()

    # Wrap solidify
    print("Wrap solidify")
    segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
    effect = segmentEditorWidget.activeEffect()
    segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('skin'))
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID) #This is important to highlight the desired segment to alter.
    effect.setParameter("region", "outerSurface")

    effect.setParameter("carveHolesInOuterSurface", True)
    effect.setParameter("carveHolesInOuterSurfaceDiameter" , 5)

    effect.setParameter("splitCavities", True)
    effect.setParameter("splitCavitiesDiameter", 5)

    effect.setParameter("createShell", True)
    effect.setParameter("shellOffsetDirection", "outside")
    effect.setParameter("shellThickness", 0.5)

    effect.setParameter("outputType", "segment")

    #segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('skin'))
    effect.self().onApply()


    # Make sure surface mesh cells are consistently oriented
    surfaceMesh = vtk.vtkPolyData()
    segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID, surfaceMesh)
    normals = vtk.vtkPolyDataNormals()
    normals.AutoOrientNormalsOn()
    normals.ConsistencyOn()
    normals.SetInputData(surfaceMesh)
    normals.Update()
    surfaceMesh = normals.GetOutput()

    # Make segmentation results visible in 3D
    segmentationNode.CreateClosedSurfaceRepresentation()
    # display()

    # Clean up
    segmentEditorwidget = None
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    # display()


    # write to PLY file
    #writer = vtk.vtkPLYWriter()
    #writer.SetInputData(surfaceMesh) 
    #writer.SetFileName("/home/raouf/Documents/UM/SEM6/FYP_3D/practical/Auto_seg_script/BrainTumor1_seg_aut.ply") 
    #writer.Update()







    ##list of parameters that can be set in wrap solidify

    ARG_DEFAULTS = {}
    ARG_OPTIONS = {}

    ARG_REGION = 'region'
    REGION_OUTER_SURFACE = 'outerSurface'
    REGION_LARGEST_CAVITY = 'largestCavity'
    REGION_SEGMENT = 'segment'
    ARG_OPTIONS[ARG_REGION] = [REGION_OUTER_SURFACE, REGION_LARGEST_CAVITY, REGION_SEGMENT]
    ARG_DEFAULTS[ARG_REGION] = REGION_OUTER_SURFACE

    ARG_REGION_SEGMENT_ID = 'regionSegmentID'
    ARG_DEFAULTS[ARG_REGION_SEGMENT_ID] = ''

    ARG_CARVE_HOLES_IN_OUTER_SURFACE = 'carveHolesInOuterSurface'
    ARG_DEFAULTS[ARG_CARVE_HOLES_IN_OUTER_SURFACE] = False

    ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER = 'carveHolesInOuterSurfaceDiameter'
    ARG_DEFAULTS[ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER] = 10.0

    ARG_SPLIT_CAVITIES = 'splitCavities'
    ARG_DEFAULTS[ARG_SPLIT_CAVITIES] = False

    ARG_SPLIT_CAVITIES_DIAMETER = 'splitCavitiesDiameter'
    ARG_DEFAULTS[ARG_SPLIT_CAVITIES_DIAMETER] = 5

    ARG_CREATE_SHELL = 'createShell'
    ARG_DEFAULTS[ARG_CREATE_SHELL] = False

    ARG_SHELL_THICKNESS = 'shellThickness'
    ARG_DEFAULTS[ARG_SHELL_THICKNESS] = 1.5

    ARG_SHELL_OFFSET_DIRECTION = 'shellOffsetDirection'
    SHELL_OFFSET_INSIDE = 'inside'
    SHELL_OFFSET_OUTSIDE = 'outside'
    ARG_OPTIONS[ARG_SHELL_OFFSET_DIRECTION] = [SHELL_OFFSET_INSIDE, SHELL_OFFSET_OUTSIDE]
    ARG_DEFAULTS[ARG_SHELL_OFFSET_DIRECTION] = SHELL_OFFSET_INSIDE

    ARG_SHELL_PRESERVE_CRACKS = 'preserveCracks'
    ARG_DEFAULTS[ARG_SHELL_PRESERVE_CRACKS] = True

    ARG_OUTPUT_TYPE = 'outputType'
    OUTPUT_SEGMENT = 'segment'
    OUTPUT_NEW_SEGMENT = 'newSegment'
    OUTPUT_MODEL = 'model'
    ARG_OPTIONS[ARG_OUTPUT_TYPE] = [OUTPUT_SEGMENT, OUTPUT_NEW_SEGMENT, OUTPUT_MODEL]
    ARG_DEFAULTS[ARG_OUTPUT_TYPE] = OUTPUT_SEGMENT

    ARG_OUTPUT_MODEL_NODE = 'WrapSolidify.OutputModelNodeID'

    ARG_REMESH_OVERSAMPLING = 'remeshOversampling'
    ARG_DEFAULTS[ARG_REMESH_OVERSAMPLING] = 1.5  # 1.5x oversampling by default

    ARG_SMOOTHING_FACTOR = 'smoothingFactor'
    ARG_DEFAULTS[ARG_SMOOTHING_FACTOR] = 0.2

    ARG_SHRINKWRAP_ITERATIONS = 'shrinkwrapIterations'
    ARG_DEFAULTS[ARG_SHRINKWRAP_ITERATIONS] = 6

    ARG_SAVE_INTERMEDIATE_RESULTS = 'saveIntermediateResults'
    ARG_DEFAULTS[ARG_SAVE_INTERMEDIATE_RESULTS] = False


sys.path.append('/home/raouf/Documents/Tools/Slicer-4.11.20200930-linux-amd64/bin/')
# print("heello")

#adding DICOM directory
dicomDataDir = "/home/raouf/Documents/UM/SEM6/FYP_3D/Datasets/custom-picked-CIA/manifest-1617532144294"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

# 
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

# having the node as variable for manipulation #TODO find a way to automatically load the first model and then load and manipulate the rest.
masterVolumeNode=getNode('3: VOLUMETRIC AXIAL_4')

skinSeg(masterVolumeNode);
