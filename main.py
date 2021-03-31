import cv2


# define function to convert captured image into canny edge form
def canny_filter(image):
    # gray scaling frame
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blur image with bilateralFilter to reduce noise and keep it's sharp edges
    img_bilateral_blur = cv2.bilateralFilter(img_gray, 9, 75, 75)
    # use canny algorithm to find the edge
    canny_edges = cv2.Canny(img_bilateral_blur, 10, 45)
    # find the threshold with invert binary
    _, mask = cv2.threshold(canny_edges, 10, 255, cv2.THRESH_BINARY_INV)

    return mask


# get video capture from webcam
capture = cv2.VideoCapture(0)

"""
read the capture in the loop,
show the frame that has filtered by canny_filter() function,
if user hit enter the program will stopped
"""
while True:
    ratio, frame = capture.read()
    cv2.imshow('Canny Filter', canny_filter(frame))
    if cv2.waitKey(1) == 13:  # 13 is code for enter key
        break

capture.release()
cv2.destroyAllWindows()
