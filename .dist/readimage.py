# Importing the OpenCV library 
import cv2 

# Reading the image using imread() function 
image = cv2.imread('Dog.jpg') 

# Extracting the height and width of an image 
h, w = image.shape[:2] 
roi = image[100 : 500, 200 : 700]

# Displaying the height and width 
print("Height = {},  Width = {}".format(h, w)) 