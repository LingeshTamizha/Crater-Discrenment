import cv2
from ultralytics import YOLO
from PIL import Image
from GetLocation import get_geo_location
from Upload import upload

model = YOLO("best.pt")

cam = cv2.VideoCapture(0)
count=0
frameno = 0
while(True):
   ret,frame = cam.read()
   if ret:
      count+=1
      if (count%20==0):
         
         name = 'temp.jpg'
         print ('new frame captured...' + name)

         cv2.imwrite(name, frame)
         results = model.predict(source="temp.jpg", show=True)
         print(results)
         if results[0].masks:
            im_array = results[0].plot()
            im = Image.fromarray(im_array[...,::-1])
            longitude,latitude=get_geo_location()
            if not(longitude or latitude):
               longitude=latitude=frameno
            im.save(f"frames\\{longitude}_{latitude}.jpg")
            upload()
      frameno += 1
   else:
      break

cam.release()
cv2.destroyAllWindows()
