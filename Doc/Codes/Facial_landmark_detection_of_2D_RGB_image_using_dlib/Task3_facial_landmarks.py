# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
# 	help="path to facial landmark predictor")
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())



def GetLandmarks(imPath,predictorPath, showImg=False, faceAndNose=True):
    #Creates an array that contains the locations of the landmarks in float.
    #
    
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictorPath)

    # load the input image, resize it, and convert it to grayscale
    image0 = cv2.imread(imPath)
    (h0, w0) = image0.shape[:2]
    width=500;
    ensmallRatio = width / float(w0)
    enlargeRatio= 1/ensmallRatio

    print("enlargeRatio: ",enlargeRatio)
    print("ensmallRatio: ", ensmallRatio)


    image = imutils.resize(image0, width=width)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 1)

    a=[-1,-1]
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the face number
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        
        counter=0
        # for (x, y) in shape:
        # 	counter=counter+1
        # 	# if faceAndNose & counter>=27 & counter<=48:
        # 	# 		print("hello")    			
        # 	# 		cv2.circle(image0, (int(x*enlargeRatio), int(y*enlargeRatio)), 3, (0, 0, 255), -1);
        # 	# 		cv2.putText(image0, "P #{}".format(counter + 1), (int(x*enlargeRatio) - 1, (int(y*enlargeRatio) - 1))  )
        # 	# 		cv2.circle(image, (x, y), 3, (0, 0, 255), -1);
        # 	# 		cv2.putText(image, "P #{}".format(counter + 1), (x - 1, y - 1))
        # 	# if not faceAndNose:
        # 	cv2.circle(image0, (int(x*enlargeRatio), int(y*enlargeRatio)), 3, (0, 0, 255), -1)
        # 	# cv2.putText(image0, "P #{}".format(counter + 1), ((int(x*enlargeRatio) - 1, (int(y*enlargeRatio) - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        # 	cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
        # 	# cv2.putText(image, "P #{}".format(counter + 1), (x - 1, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1);#hwl
        # 	a=np.vstack([a, [x*enlargeRatio, y*enlargeRatio]]) # a is not integer so be aware.
        # print(np.shape(a))
        for (x,y) in shape:
                counter=counter+1
                if not faceAndNose:
                    cv2.circle(image, (int(x), int(y)), 3, (0, 0, 255), -1)
                    cv2.putText(image, "#{}".format(counter), (x - 1, y - 1),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(image0, (int(x*enlargeRatio), int(y*enlargeRatio)), 3, (0, 0, 255), -1)
                    cv2.putText(image0, "#{}".format(counter), (int(x*enlargeRatio), int(y*enlargeRatio)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    a=np.vstack([a, [x*enlargeRatio,y*enlargeRatio]])

                if faceAndNose & (counter>=28) & (counter<=48):
                    #print(counter)
                    cv2.circle(image, (int(x), int(y)), 3, (0, 0, 255), -1)
                    cv2.putText(image, "#{}".format(counter), (x - 1, y - 1),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.circle(image0, (int(x*enlargeRatio), int(y*enlargeRatio)), 3, (0, 0, 255), -1)
                    cv2.putText(image0, "#{}".format(counter), (int(x*enlargeRatio), int(y*enlargeRatio)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    a=np.vstack([a, [x*enlargeRatio,y*enlargeRatio]])
                
    # show the output image with the face detections + facial landmarks
    a=np.delete(a, 0, 0);

    if showImg:
        #small image
        cv2.imshow("Original", image0)
        cv2.imshow("downSized", image)
        #cv2.imshow("output",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #originalImage:
        #a=a*enlargeRatio;
    print("np.shape(a) :",np.shape(a))
    return a 

#example code : python facial_landmarks.py --shape-predictor Data/Model_Predictor/shape_predictor_68_face_landmarks.dat --image Data/imgs/Test4.png
