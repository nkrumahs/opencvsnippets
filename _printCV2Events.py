import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
for event in events:
    print(event)
