import os
import cv2 as cv

File_object = open("dirName.txt","r")
dir= File_object.readline();
solo=0
group=0
obj=0

haar_cascade= cv.CascadeClassifier('.\haar_face.xml');
for filename in os.listdir(dir):
    if filename.endswith(".jpg"): 
        pathname=os.path.join(dir,filename);
        img=cv.imread(pathname);
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY);
        faces=haar_cascade.detectMultiScale(gray,1.3,5);
        #uncomment lines 18-19 to draw on the faces detected, add cv.imshow as needed
        # for (x,y,w,h) in faces:
        #     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
        if(len(faces)==0):
            obj+=1;
        elif(len(faces)==1):
            solo+=1;
        else:
            group+=1;
    else:
        continue
print(f'Pictures read :{solo+group+obj}');
print(f'Solo pictures :{solo}');
print(f'Group pictures :{group}');
print(f'Abstract pictures :{obj}');


cv.waitKey(0)
