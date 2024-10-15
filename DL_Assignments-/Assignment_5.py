#Text Identification Using OpenCV and Tesseract (OCR)

import cv2
import pytesseract

# Load an image with text
img = cv2.imread('text_image.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use Tesseract OCR
text = pytesseract.image_to_string(gray)
print("Identified Text:", text)

# Show the image
cv2.imshow('Text Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
