import numpy as np
import random
from shapely.geometry import Polygon, Point

poly = Polygon([(49.938255661363215, 1.5801288804843638), (44.669952201777605, 2.283253880484364),(47.14614010899952, 22.014699192984363),(53.91835702679154, 18.982472630484363)])

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)
    return points
# Choose the number of points desired. This example uses 20 points. 
points = polygon_random_points(poly,5)


# Printing the results.
for p in points:
    print([p.x,p.y])