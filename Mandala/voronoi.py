from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi

def main ():
    itr=3          # iterations
    points=6      # number of initial voronoi points
    radius=2       # the rate of expansion/compression
    bounds=(10,10) # the bounds of the figure
    build_mandala(itr,points,radius,bounds)


"""
builds you a mandala
"""
def build_mandala(iterations:int, points:int, radius:float,bounds:(int, int)):
    angles = get_angles(points)
    coordinates=iterate_and_get_points_for_mandala(iterations, angles, radius)
    # creates a voronoi object based on the co-ordinates
    print(coordinates)
    mandala = Voronoi(coordinates)
    voronoi_plot_2d(mandala, show_points=False, show_vertices=False, dpi=1200,)
    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('mandala3.png')
    return plt.show()

"""
basically iterates over the centres and creates more points/centres for mandala
so that it can finally be graphed as a voronoi space
"""
def iterate_and_get_points_for_mandala(iterations:int, angles, radius:float):
    x,y=0,0
    coordinates = pd.DataFrame([[x,y]], columns=['x','y']) 
    for iteration in range(iterations):
        print(f'iteration {iteration}:')
        points_on_x, points_on_y = np.array([]), np.array([])
        for row in range(coordinates.shape[0]):
            xval, yval=calculate_location(coordinates,radius, angles,row,iteration)
            points_on_x=np.append(points_on_x,xval)
            points_on_y=np.append(points_on_y,yval)
        points=np.column_stack((points_on_x,points_on_y))
        coordinates=pd.DataFrame(points, columns=['x','y'])
    return coordinates    

"""
returns an np.array of all the possible angles, given the number of points
"""
def get_angles(points,x=0,y=0):
    return np.linspace(0,2*pi,points+1)[:-1]

"""
calculates normalised location of a possible center
"""
def calculate_location (dataframe,radius,angles,row,iteration):
    return dataframe['x'][row]+(radius**iteration)*np.sin(angles),dataframe['y'][row]+(radius**iteration)*np.cos(angles)

if __name__ == '__main__':
    main()
