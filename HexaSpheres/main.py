import matplotlib.pyplot as plt
import numpy as np
from math import pi

class Circles:
    def __init__ (self, centers,radius,factor=0.85):
        self.centers=centers[:]
        self.radius=radius
        self.factor=factor
    def modify_radius(self):
        self.radius=self.radius*self.factor
    def get_coordinates(self):
        return self.coordinates
    def copy(self):
        return Circles(self.centers[:],self.radius,self.factor)
    def move_centers(self, by):
        for i in range(len(self.centers)):
            self.centers[i]=tuple(map(op('+'),self.centers[i],by))
    def get_cols (self):
        return np.column_stack(self.centers)

def op(f):
    return eval(f"lambda x,y:x{f}y")

def main():
    display(get_centers(3))

def get_centers(iterations=5,origin=(0,0),circles=5,radius=5,):
    centers=Circles([origin],radius)
    for j in range(iterations):
        print(j)
        all_new_centers=[]
        for i in range(5):
            new_centers=centers.copy()
            new_centers.modify_radius()
            c=2.7**(j)
            if not j:
                c=1
            new_centers.move_centers((radius*c*np.sin(2*pi*(i/5)),radius*c*np.cos(2*pi*(i/5))))
            all_new_centers.append(new_centers)
            if j > 0 and None:
                break
        centers=build(all_new_centers)
    return centers

def build (centers):
    cumul=[]
    for circles in centers:
        cumul+=circles.centers[:]
    return Circles(cumul, centers[0].radius,centers[0].factor)

def display(circles):
    for center in circles.centers:
        c=plt.Circle(center,radius=circles.radius,fill=False)
        plt.gca().add_artist(c)
    plt.axis('equal')
    plt.axis([-300,300,-300,300])
#   plt.scatter(*centers.get_cols())
    plt.show()
if __name__=='__main__':
    main()
