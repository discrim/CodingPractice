import cv2

img = cv2.imread('Capture.png', cv2.IMREAD_UNCHANGED)

print('Original Dimensions: ', img.shape)

dim = (100, 100)    # Must be a tuple

resized = cv2.resize(img, dim)

print('Resized Dimensions: ', resized.shape)

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
