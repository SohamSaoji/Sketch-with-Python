#import library
import cv2

# read image
image = cv2.imread("image3.jpg")

#convert image to grey scale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# invert the image
inverted = cv2.bitwise_not(gray_image)

#blur the image by gaussian blur function
blurred_image = cv2.GaussianBlur(inverted,(21,21),0)

#invert the image
invertedBlur = 255-blurred_image

#create pencil sketch image
pencilSketch = cv2.divide(gray_image,invertedBlur,scale=256.0)


#save the pencil sketch image
cv2.imwrite("img5.jpg",pencilSketch)