import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Delaunay, delaunay_plot_2d
from random import sample
from PIL import Image
import pandas as pd

FNAME='def.png'
IMG=cv.imread(FNAME)
def main():
    get_black_points(IMG,80,2500)
    #Image.open('./output.png').show()

def get_black_points (image,threshold=100,samples=10000):
    gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    (thresh, bw) = cv.threshold(gray_image,threshold,255,cv.THRESH_BINARY)
    blackpoints=[]
    for x,_ in enumerate(bw):
        for y,_ in enumerate(bw[x]):
            if bw[x][y] == 0:
                blackpoints.append((float(y),-float(x)))
    print(bw.shape)
    points=np.column_stack(sample(blackpoints,samples))
    points=np.transpose(points)
    print(points)
    points=pd.DataFrame(points,columns=['x','y'])
    print(points)
    create_delaunay_portrait(points)
    #cv.imwrite('./output.png',bw)

def create_voronoi_portrait (coordinates):
    print('shape:',coordinates.shape)
    mandala = Voronoi(coordinates)
    voronoi_plot_2d(mandala, show_points=False, show_vertices=False,line_width=0.5, )
    plt.axis('off')
    plt.gca().set_aspect('equal',adjustable='box')
    plt.savefig('voronoi.png')
    return plt.show()
 
def create_delaunay_portrait (coordinates):
    print('shape:',coordinates.shape)
    mandala = Delaunay(coordinates)
    coordinates=np.array(coordinates)
    plt.triplot(coordinates[:,0],coordinates[:,1],mandala.simplices,linewidth=1)
    plt.axis('off')
    plt.gca().set_aspect('equal',adjustable='box')
    plt.savefig('delaunay.png')
    return plt.show()
   
if __name__ == '__main__':
    main()
