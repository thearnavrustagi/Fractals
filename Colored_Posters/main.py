import numpy as np
import cv2 as cv
import sys
import matplotlib.pyplot as plt

FNAME='./def.png' if len(sys.argv) < 2 else sys.argv[1]
print('file:',FNAME)
GCD=40 if len(sys.argv) < 3 else int(sys.argv[2])
IMG=cv.imread(FNAME)

def main(out='./output1.png',file=None):
    print(IMG)
    image=build_portrait(IMG,_min=0.3,_max=0.4,color=(0,122,255),gcd=GCD)
    cv.imwrite(out,image)

def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

def op (s):
    return eval(f'lambda x,y:x{s}y')

def build_portrait (image,min_row_squares=20,_min=0.15,_max=0.4,gcd=15,color=(0,0,0)):
    modified_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    image=np.copy(modified_image)
    #hcf(*modified_image.shape)
    width,height=image.shape[0],image.shape[1]
    #while min(modified_image.shape)/gcd < min_row_squares:
    #    print(modified_image.shape,gcd)
    #    gcd/=2
    b_width,b_height=int(width/gcd),int(height/gcd)
    print(gcd,gcd)
    boxes=cv.resize(modified_image,(b_height,b_width))#tuple(map(op('/'),image.shape,(gcd,gcd))))
    Y=modified_image.shape[1]
    image = cv.cvtColor(image,cv.COLOR_GRAY2RGB)
    for y in range(len(boxes)):
        for x in range(len(boxes[y])):
            padding=min(max(boxes[y][x]/510,_min),_max)
            pt1=(int(((x+padding)*gcd)),int((y+padding)*gcd))
            pt2=(int(((x+1-padding)*gcd)),int((y+1-padding)*gcd))
            cv.rectangle(image,pt1=pt1,pt2=pt2,color=color,thickness=-1)
    return image

if __name__ == '__main__':
    main()
