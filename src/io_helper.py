import pandas as pd
import numpy as np
import create_circle
def read_tsp(filename):
    with open(filename) as f:
        node_coord_start = None
        dimension = None
        num_robot = None
        node_robot_start = None
        lines = f.readlines()

        i = 0
        while not dimension or not node_coord_start or not num_robot or not node_robot_start:
            line = lines[i]
            print(line)
            if line.startswith('DIMENSION :'):
                dimension = int(line.split()[-1])
            if line.startswith('NODE_COORD_SECTION'):
                node_coord_start = i
            if line.startswith("ROBOT :"):
                num_robot = int(line.split()[-1])
            if line.startswith("ROBOT_BUDGET_SECTION"):
                node_robot_start = i
            i = i+1

        print('Problem with {} cities read.'.format(dimension))

        f.seek(0)

        robots = pd.read_csv(
            f,
            skiprows=node_robot_start + 1,
            sep=' ',
            names=['inx', 'budget'],
            dtype={'idx': str, 'budget': np.float64},
            header=None,
            nrows=num_robot
        )

        f.seek(0)

        # Read a data frame out of the file descriptor
        cities = pd.read_csv(
            f,
            skiprows=node_coord_start + 1,
            sep=' ',
            names=['city', 'x', 'y', 'r'],
            dtype={'city': str, 'x': np.float64, 'y': np.float64, 'r': np.float64},
            header=None,
            nrows=dimension
        )

        # cities.set_index('city', inplace=True)

        return cities[['x', 'y', 'r']].to_numpy(), robots[['budget']].to_numpy()

def normalize(points):
    # ratio = (points.x.max() - points.x.min()) / (points.y.max() - points.y.min()), 1
    # ratio = np.array(ratio) / max(ratio)
    # norm = points.apply(lambda c: (c - c.min()) / (c.max() - c.min()))
    # return norm.apply(lambda p: ratio * p, axis=1)
    points[:,:] /= create_circle.MAX_SIZE
