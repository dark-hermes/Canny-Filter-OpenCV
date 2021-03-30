import cv2
import numpy as np

# define function to convert captured image into canny edge form
def canny_filter(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    img_bilateral_blur = cv2.bilateralFilter(img_gray, 9,75,75)

    canny_edges = cv2.Canny(img_bilateral_blur, 10,45)
    
    _, mask = cv2.threshold(canny_edges, 10,255, cv2.THRESH_BINARY_INV)
    
    return mask

capture = cv2.VideoCapture(0)

while True:
    ratio, frame = capture.read()
    cv2.imshow('Canny Filter', canny_filter(frame))
    if cv2.waitKey(1) == 13:
        break
        
capture.release()
cv2.destroyAllWindows()

