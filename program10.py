#Write a program to blur and smoothing an image.
import cv2
# Load the image
image = cv2.imread(r'H:/Drone Data/India/West India/Rajkot/Science Center/DJI_20240519173357_0021_D.JPG')
# Replace with the path to your image C:/Users/mrchi/Desktop/face.jpeg
# Check if the image was successfully loaded 
if image is None:
 print("Error: Could not load image.")
 exit()
# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
# Median Blur
median_blur = cv2.medianBlur(image, 5)
# Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)
# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_filter)
# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()