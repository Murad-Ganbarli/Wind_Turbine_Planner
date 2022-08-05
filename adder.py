import numpy as np 
import cv2
from PIL import Image
import os
def draw_circle(event,x,y, flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),radius=5,color=(255, 255 ,255 ) ,thickness=-1 )
        mouseX,mouseY = x,img.shape[0]-y
        #print(img.shape , img.shape[0] , img.shape[1])
        coords=[ S+(N-S)*mouseY/img.shape[1],  W+(E-W)*mouseX/img.shape[1] ] 
        print("Point",len(list)+1,  round(coords[0], ACC) , round(coords[1] , ACC))
        #print(x, y)
        list.append(coords  )
def adder( s,n,w,e , dir=os.path.dirname(os.path.realpath(__file__)), img_path=os.getcwd()+'/images/area.png',diameter=5, color=(0,0,0), acc=4 ):
    global list
    list=[]
    im=Image.open(img_path)
    global img, saved, S, N,W,E ,ACC
    S=s 
    N=n
    W=w
    E=e
    ACC=acc
    img=np.asarray(im)
    cv2.namedWindow("AREA")
    cv2.setMouseCallback("AREA",draw_circle)
    while(1):      
        cv2.imshow("AREA",img)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('s') or k==ord('S'):
            Image.fromarray(img).save( os.getcwd()+'/images/marked.png')
            break
    return list
#For test:
if __name__ == '__main__':
    diameter=5
    color=(250,245,23)
    path=os.getcwd()+ '/images/image.png'
    s , w= 46.7384,39.75
    n, e= 46.7408 , 39.7515

    output=adder(dir, path ,diameter, color, s,n, w,e)
    print(output)