# pip install opencv-python
import cv2   # Use to import opencv-python

# OPENCV in PYTHON
""""
# Load the image
image = cv2.imread("jg.png")

# Display the image
cv2.imshow("Image", image)

# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
"""


# Configurable Parameters
source="dragon-ball-super-son-goku-super-saiyan-god-dragon-ball-wallpaper.jpg"
destination="output.jpeg"
# percentage by which image is resized
scale_percent=25


src=cv2.imread(source)
cv2.imshow("title",src)
cv2.waitKey(0)


# hieght is given by [0] and width is given by [1]
new_width=int(src.shape[1]*scale_percent/100)
new_hieght=int(src.shape[0]*scale_percent/100)
""""   50 percent of original dimension = original shape* scale percent /100       """

# to decrease size-->
d_size=(new_width,new_hieght)

# To resize our image
output=cv2.resize(src,d_size)


# to export our file
cv2.imwrite(destination,output)
src2=cv2.imread("output.jpeg")
cv2.imshow("title1",src2)
cv2.waitKey(0)