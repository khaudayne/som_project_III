import numpy as np
import math
import random
from distance import select_closest

def generate_network(robots, problem, multi = 2):
    number_robot = len(robots)
    number_waypoint = math.ceil(len(problem) / number_robot)
    network = [[]] * number_robot
    for i in range(number_robot):
        tmp_list = []
        radius = problem[i][2] * multi
        for j in range(number_waypoint):
            tmp_random = random.random()
            tmp_list.append(
                [
                    problem[i][0] + radius * tmp_random
                    , problem[i][1] + radius * math.sqrt(1 - tmp_random * tmp_random)
                ])
        network[i] = tmp_list
    return network

def get_neighborhood(center, radix, domain):
    # Impose an upper bound on the radix to prevent NaN and blocks
    if radix < 1:
        radix = 1

    # Compute the circular network distance to the center
    deltas = np.absolute(center - np.arange(domain))
    distances = np.minimum(deltas, domain - deltas)

    # Compute Gaussian distribution around the given center
    return np.exp(-(distances*distances) / (2*(radix*radix)))

# cities là dataframe, network là mạng random ngẫu nhiên ban đầu (hay là đường đi cho robot ban đầu)
def get_route(cities, network):
    cities['winner'] = cities[['x', 'y']].apply(
        lambda c: select_closest(network, c),
        axis=1, raw=True)

    # Hàm sort_value sẽ sort các data column theo thuộc tính args, index trả về list [] label column của chúng
    return cities.sort_values('winner').index

def adaption(path, city, sigma):
    pass

def regeneration(network):
    pass

def cal_score(problem, network):
    pass