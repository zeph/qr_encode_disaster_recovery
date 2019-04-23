from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
 
def decode(im) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)
 
  # Print results
  for obj in decodedObjects:
    print(obj.data.decode('ascii'))

  return decodedObjects
 
 
# Display barcode and QR code location  
def display(im, decodedObjects):
 
  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;
     
    # Number of points in the convex hull
    n = len(hull)
 
    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
 
  # Display results 
  cv2.imshow("Results", im);
  cv2.waitKey(50);
 
   
# Main 
if __name__ == '__main__':
 
  # Read image
  cap = cv2.VideoCapture(0)
  while(1):

    # Take each frame
    _, frame = cap.read()
    decodedObjects = decode(frame)
    display(frame, decodedObjects)
    if len(decodedObjects) > 0:
          cv2.waitKey(0);

