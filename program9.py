#Read an image and extract and display low-level features such as edges, textures using filtering techniques.
import cv2
import numpy as np
# Load the image
image_path = r"H:/Drone Data/India/West India/Rajkot/Science Center/DJI_20240519173357_0021_D.JPG" 
# Replace with the path to your image C:/Users/mrchi/Desktop/face.jpeg
img = cv2.imread(image_path)
# Check if the image was successfully loaded
if img is None:
 print("Error: Could not load image.")
 exit()
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Edge detection using Canny edge detector
edges = cv2.Canny(gray, 100, 200)
# Texture extraction using an averaging filter
kernel = np.ones((5, 5), np.float32) / 25 
# Define a 5x5 averaging kernel
texture = cv2.filter2D(gray, -1, kernel) 
# Apply the averaging filter for texture extraction
# Display the original image, edges, and texture
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Texture", texture)
# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()