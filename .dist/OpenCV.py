import cv2
import os

#loads an image
def Load():
    print("Files:")
    print(os.listdir('D:\OpenCV'))
    load_image = input("Enter file name:")
    while not os.path.isfile(load_image):
        print("Image doesn't exist")
        break
    else:
        cv2.imread(load_image, 1)
        print("Done!")
    switch()

#saves a file image
def Save():
    load_image = input("Enter original file name:")
    new_image = cv2.imread(load_image, 1)
    new_name= input("Enter new file name:")
    cv2.imwrite(new_name,new_image)
    switch()

#displays an image
def Display():
    image_name = input("Enter image name:")
    img= cv2.imread(image_name, 1)
    while os.path.isfile(image_name):
        cv2.imshow('Image', img)
        print("Image is displayed!")
        k = cv2.waitKey(0) & 0xFF
# wait for ESC key to exit
        if k == 27: 
            cv2.destroyAllWindows()
        break  
    else:
        print("Image doesn't exist")
         
        switch()
    
#this function contains the list of commands, this is where the user choose a command
def switch():
    print("List of Commands: \n 1) Load Image \n 2) Save Image \n 3) Display Image")
    command = int(input("Enter an integer:"))
        
    dict = {
        1 : Load,
        2 : Save,
        3 : Display,
 
    }
    dict.get(command)() # get() method returns the function matching the argument
 
switch() # Call switch() method
    
