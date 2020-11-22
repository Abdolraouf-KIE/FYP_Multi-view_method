# Guids for Documentation
Overall goal, approach, high-level plan
execution control meeting
1. Review what was done vs. planned, check if help needed => update issues, add notes.
2. Update short-term plan (2 weeks) => update project board.
3. Check if long-term plan is still OK => update plan
<br>

1. Software documentation
2. Entering a bug report: What did you do? What did you expect? What happened instead? Attach logs, screenshot.
3. Add comment whenever making progress
4. Projects:
   - Columns on the project board
   - To do: when tasks are completed, we choose what to do next from this column.
   - In progress: currently somebody working on it; make sure somebody is assigned.
   - Done: closed issues, no further action is planned.
   - To test: useful for projects where users and developers are different group.
   - Future: collection of ideas for the future
5. Releases 
   - Supports upfront planning and monitoring progress
   - The way to define deadlines (no deadlines for individual tickets)
   - Files can be attached (e.g., installation package)
6. Refer to issues if your commit is fixing/addresing it. use re #123

# Overall Goal

## Topic
Automatic registration for Image guided surgery for brain tumor resection

## Title
Automated surface-based intraoperative registration for brain tumor resection using machine learning
<br>Elements:

1. Automated surface Segmentation: Using CNN model that can determine a given feature (e.g. contour of eye)→ outputs feature parameters
2. image processing: Mapping patient face and creating a surface point cloud
3. Registration: of the intraoperative and preoperative point clouds

## Background
With the progress in computer image vision technology, the mapping technique based on optical data has developed specially in the medical imaging field. One of the techniques used in mapping technology is use of stereoscopic cameras for surface-based registration, which is then visualized by overlaying it on 3D preoperative data (MRI, or CT) using either manual or automatic process. It is an interest to have a real-time automatic registration where traditional methods are inadequate.

## Problem Statement 
Traditional techniques make use of iterations and this manner is very slow where runtime in the tens of minutes are normal for common deformable image registration techniques even with an efficient implementation on the contemporary GPUs; while the practical use in clinical operations is real-time, and such a prolonged wasting time is not appreciated. This paper proposes utilizing deep learning to carry out the registration.

## Objectives

1. Evaluate the need for machine learning registration over traditional registration of surfaces.
2. Evaluate a technique for segmentation of face from the rest of head model.
3. Use reliable NN model (CNN or SAE or GAN or RNN or DRL) for registration based on facial features
4. Demo Registration with control model (control is the unsegmented model)

(Extra)
- Obtain 3D map of the face
- Carryout registration based on extracted feature

## Expected Outcome
- Segment the desired feature from the model to be used for registration.
- Determine an evaluation metric and method for the registration.
- Set desired accuracy for model.
- Carryout registration of (pre-segmented) face
