# Components of 2D method:

The 2D method is made up of 4 major tasks:

1. **Task1_Load&Segment:** loading dicom flies and then automatically segmenting them. The result is a model in the scene. 
2. **Task2_Capture_image_3DSlicer:** Capture an image of the viewpoert and save it inside a folder. Camera mipulation must be done before capturing image.
3. **Task2_b_Capture_iamge_Bledner:** Capture an image of the viewport of blender and save it inside a folder. Camera mipulation must be done before capturing image.
4. **Task3_facial_landmarks:** take an image and find the landmarks on face. landmarks are savedas an array of [x,y]. Uses venv
5. **Task4: proejct_landmarks** takes an x and y value (of the display/viewport) and finds the corresponding 3D point in 3D slicer. At this point a fiducial is placed.

Each of the tasks will have thier own .py file and they are tested seperatly by copying the codes in the file into the python interpreter of 3DSlcier. For future use a full script can be developed to be run using "Slicer -c ./script.py" in ubuntu without having to open the slicer software.

references used to accomplish each task as well as other relevant information are given below.

## references for coding with 3D Slicer:

Introduction to 3DSlicer components (Developer description only):
- https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html

Introduction to 3DSlicer components (User guide):
- https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html

Coordiante system in 3DSlicer:
- https://www.slicer.org/wiki/Coordinate_systems

3DSlicer discourese:
- https://discourse.slicer.org/search?q=picker

ScriptRepositiry:
- https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository

Using Python interpreter guides: (very useful in using slicer exisiting GUI features)
- https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python
- https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features

## Task1: Load and Segment

## Task2: Capture image

Camera Manipulation:
- https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras

Capture:
- https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/ScreenCapture/ScreenCapture.py
- https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture

## Task3: Facial Landamrk detection

This sectioin uses virtual environment with dlib to obtain the landmarks.

## Task4: projection of landmarks

### point picking
The projection part of this task can be carried out using the following methods:
1. Using vtk picking functions (without 3DSlcier):
   - https://vtk.org/Wiki/VTK/Examples/Python/Interaction/HighlightAPickedActor
   - https://vtk.org/Wiki/VTK/Examples/Cxx/Interaction/PointPicker
   - https://vtk.org/doc/nightly/html/classvtkPointPicker.html#ad7d175f4812e135ffb98bdb7c5750534
2. Using vtk picking functions (in 3DSlcier's [MRMLModelDisplayableManager](https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/MRML/DisplayableManager/vtkMRMLModelDisplayableManager.cxx) node):
   - [Example](https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_segments_visible_at_a_selected_position) use of 2DDisplaymodelManager
   - [Example](https://discourse.slicer.org/t/how-to-create-a-fiducial-though-the-pixel-not-the-mouse-event/11410) use of pick() fucntion.
3. Using fucntions in vtkMRMLAnnotationDisplayableManager.cxx:
   1. [vtkMRMLAnnotationDisplayableManager.cxx](https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Loadable/Annotations/MRMLDM/vtkMRMLAnnotationDisplayableManager.cxx)
      - GetDisplayToWorldCoordinates()
      - OnClickInRenderWindowGetCoordinates()
We might need to find the closest point, if so refer to Getclosestpoint() in:
- https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode


### Adding fiducials at given ras value:
1. https://apidocs.slicer.org/v4.8/classvtkSlicerAnnotationModuleLogic.html#a3d2512ff6614b57a47388d7f924f57c6ac046ece1ebad0090a086c98bf3dfd7ed
2. https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Base/Logic/vtkSlicerFiducialsLogic.h
3. https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Adding_Fiducials_Programatically




# Other useful functions and Scripts:

1. Get centroid of a segment in world (RAS) coordinates
   - https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_(RAS)_coordinates
2. Access to Fiducial properties:
   - https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_to_Fiducial_Properties