import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Delaunay, delaunay_plot_2d
from random import sample
from PIL import Image
import pandas as pd

FNAME = "def.png"
IMG = cv.imread(FNAME)


def main():
    points = get_black_points(IMG, samples=2000)
    create_voronoi_portrait(points)
    create_delaunay_portrait(points)
    # Image.open('./output.png').show()


def get_black_points(image, threshold=100, samples=10000):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    (thresh, bw) = cv.threshold(gray_image, threshold, 255, cv.THRESH_BINARY)
    blackpoints = []
    for x, _ in enumerate(bw):
        for y, _ in enumerate(bw[x]):
            if bw[x][y] == 0:
                blackpoints.append((float(y), -float(x)))
    points = np.column_stack(sample(blackpoints, samples))
    points = np.transpose(points)
    points = pd.DataFrame(points, columns=["x", "y"])
    return points
    # cv.imwrite('./output.png',bw)


def create_voronoi_portrait(coordinates):
    print("shape:", coordinates.shape)
    mandala = Voronoi(coordinates)
    voronoi_plot_2d(
        mandala,
        show_points=False,
        show_vertices=False,
        line_width=0.5,
        color="#6901ba",
    )
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")
    #    plt.axes().set_facecolor('#6901ba')
    plt.savefig("voronoi.svg")
    plt.clf()
    # return plt.show()


def create_delaunay_portrait(coordinates):
    print("shape:", coordinates.shape)
    mandala = Delaunay(coordinates)
    coordinates = np.array(coordinates)
    plt.triplot(coordinates[:, 0], coordinates[:, 1], mandala.simplices, linewidth=0.5)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.savefig("delaunay.svg")
    # return plt.show()


def create_spline_portrait(coordinates):
    print("shape:", coordinates.shape)
    coordinates = chaikins_corner_cutting(np.array(coordinates), 0)
    cstack = np.column_stack(coordinates)
    x, y = cstack[0], cstack[1]
    plt.plot(x, y)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.savefig("spline.png")
    return plt.show()


def chaikins_corner_cutting(coords, refinements=5):
    coords = np.array(coords)

    for _ in range(refinements):
        L = coords.repeat(2, axis=0)
        R = np.empty_like(L)
        R[0] = L[0]
        R[2::2] = L[1:-1:2]
        R[1:-1:2] = L[2::2]
        R[-1] = L[-1]
        coords = L * 0.75 + R * 0.25

    return coords


if __name__ == "__main__":
    main()
