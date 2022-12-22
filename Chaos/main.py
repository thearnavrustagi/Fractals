import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

from math import pi
from random import uniform, choice


def main():
    points = 8
    radius = 3
    coordinates = generate_chaos()
    display(coordinates)


def op(f):
    return eval(f"lambda x,y:x{f}y")


def generate_chaos(
    iterations=10000, points=5, radius=5, origin=(0, 0)
):  # ,max_depth=1,depth=0):
    shape_coordinates = get_coordinates_for_shape(points, radius, origin)
    printing_coordinates = shape_coordinates[:]
    initial_center = origin  # (uniform(-2.5,2.5),uniform(-2.5,2.5))
    center_for_fractal = initial_center
    for i in range(iterations):
        center_for_fractal = generate_next_center(center_for_fractal, shape_coordinates)
        if center_for_fractal not in printing_coordinates:
            printing_coordinates.append(center_for_fractal)
    #    for center in printing_coordinates[:]:
    #        printing_coordinates += generate_chaos(iterations,points,radius,tuple(map(op('+'),origin,center)),max_depth,depth+1)
    return printing_coordinates


"""
This function gets the co-ordinates of the vertices based on
the fact that the center is (0,0)
args:
    - points:int        number of vertices
    - radius:int        the radius of the bounding circle
    - origin:tuple(int) the origin of the shape
returns:
    coordinates:list[tuple] of form
       [(x1,y1),(x2,y2) ... (xn,yn)]
"""


def get_coordinates_for_shape(points: int, radius: int, origin=(0, 0)):
    all_x, all_y = [], []
    angle = (2 * pi) / points
    coordinates = []
    for i in range(points):
        x = radius * np.sin(i * angle)
        y = radius * np.cos(i * angle)
        coordinates.append((origin[0] + x, origin[1] + y))
    # plt.scatter(all_x,all_y)
    # plt.show()
    return coordinates


def generate_next_center(center, coordinates):
    vertice_1 = choice(coordinates)
    vertice_2 = None
    while not vertice_2 or vertice_2 == vertice_1:
        vertice_2 = choice(coordinates)

    # get midpoints from the center to the vertices
    midpoint_with_vertice = tuple(map(lambda x, y: (x - y) / 2, vertice_1, center))
    midpoint_with_midpoint = tuple(
        map(lambda x, y: (x - y) / 2, vertice_2, midpoint_with_vertice)
    )

    return midpoint_with_midpoint


def display(coordinates, voronoi=False, dela=False):
    if voronoi:
        v = Voronoi(coordinates)
        voronoi_plot_2d(v)
    elif dela:
        dela = Delaunay(coordinates)
        print(dela.simplices)
        coordinates = np.array(coordinates)
        plt.triplot(coordinates[:, 0], coordinates[:, 1], dela.simplices)

    else:
        coordinate_stack = np.column_stack(coordinates)
        plt.scatter(*coordinate_stack, 1)
    plt.show()


if __name__ == "__main__":
    main()
