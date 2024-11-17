import numpy as np

def select_closest(candidates, origin):
    return euclidean_distance(candidates, origin).argmin()

def euclidean_distance(a, b):
    return np.linalg.norm(a - b, axis=1)

def route_distance(cities):
    points = cities[['x', 'y']]
    # Roll các phần tử lên 1 để tính khoảng cách giữa dãy điểm liên tiếp
    distances = euclidean_distance(points, np.roll(points, 1, axis=0))
    return np.sum(distances)

