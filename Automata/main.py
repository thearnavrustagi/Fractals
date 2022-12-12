import numpy as np
from random import randint
import cv2 as cv

def main ():
    generate_automata((640,640),5,5,[
        rgb('F7F6CF'),
        rgb('F4CFDF'),
        rgb('B6D8F2'),
        rgb('9AC8EB'),
        rgb('5784BA'),
        ])

def rgb(h):
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def op(s):
    return eval(f'lambda x,y:x{s}y')

def generate_automata(shape=(128,128),max_value=5,iterations=5,colors=None):
    automata=initialise_automata(shape,max_value-1)
    image=[]
    for i in range(shape[0]):
        image.append(list())
        for j in range(shape[1]):
            image[i].append(list())

    if not colors:
        colors=np.linspace(0,255,max_value)
    
    neighbours=[
            (1,0),(0,1),(0,-1),(-1,0),
            (1,1),(1,1),(1,-1),(-1,1),
            ]
    for i in range(1,iterations+1):
        for x in range(len(automata)):
            for y in range(len(automata)):
                automata[x][y]=modify_automata(automata,x,y,6,neighbours=neighbours)%max_value
                image[x][y]=colors[int(automata[x][y])]
        print(f'iteration: {i}')
    cv.imwrite('./output.png',np.array(image))
    
def initialise_automata(shape,max_value):
    image=np.zeros(shape)
    
    for x in range(len(image)):
        for y in range(len(image[x])):
            image[x][y] = randint(0,max_value)
    return image

def tadd (x,y):
    return (x[0]+y[0],x[1]+y[1])

def modify_automata(automata,x,y,threshold=2,compare=None,neighbours=[(1,0),(0,1),(0,-1),(-1,0)]):
    count=0
    if not compare:
        compare = lambda x,y : x-y==1
    neighbourhood=list(map(tadd,[(x,y)]*len(neighbours),neighbours))

    for i,j in neighbourhood:
        if i < 0 or j < 0 or i >= len(automata) or j >= len(automata[0]):
            continue
        count += 1 if compare(automata[i][j],automata[x][y]) else 0
    if count >= threshold:
        return automata[x][y]+1
    return automata[x][y]

if __name__ == '__main__':
    main()
