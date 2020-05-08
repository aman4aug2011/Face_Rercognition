import face_recognition as fr
import cv2
import numpy as np
video_capture=cv2.VideoCapture(0)
priya=fr.load_image_file("F:\pro.jpg")
priya_encod=fr.face_encodings(priya)
dad=fr.load_image_file("F:\dad.jpg")
dad_encod=fr.face_encodings(dad)
known_face_encodings=[priya_encod,dad_encod]
known_face_names=["Priyansh","Mukesh"]

this_process=True
face_names=[]
face_locations=[]
face_encodings=[]

i=0

while True:
    ret,frame=video_capture.read()
    re=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb2bgr=re[:,:,::-1]
    if(this_process):        
        face_encod=fr.face_encodings(rgb2bgr)
        face_locations=fr.face_locations(rgb2bgr)
        face_names=[]
        for fe in face_encod:        
            matches=fr.compare_faces(known_face_encodings,fe)
            name="unknown"
            
            face_dist=fr.face_distance(known_face_encodings,fe)
            index=np.argmin(face_dist)
            if(matches[index]):
                name=know_face_names[index]
            face_names.append(name)
            
        i==1
        if i==5:
            print(name)
        if len(face_names)==0:
            i=0
            
        this_process= not this_process
        
        for (top,right,bottom,left),name in zip(face_locations, face_names):
            top*=4
            bottom*=4
            right*=4
            left*=4
        
            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),3)
            cv2.putText(frame,name,(left-6,bottom-6),(255,255,255),1)
        
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
video_capture.release()
cv2.destroyAllWindows()
        