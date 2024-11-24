from sys import argv

import numpy as np
import copy
import random
from io_helper import read_tsp, normalize
from neuron import generate_network, adaption, regeneration, cal_score
from distance import cal_cost
from plot import plot_network, plot_route, plot_map_circle
import create_circle
def main():
    if len(argv) != 2:
        return -1

    problem, robots = read_tsp(argv[1])

    print("\nRobots: ")
    print(robots)

    print("\Problem: ")
    print(problem)

    routes = som(problem, robots, 100000)
    print("\nRoutes: ")
    print(routes)

    for robot in range(len(routes)):
        cost = cal_cost(routes[robot])
        print("Cost of robot {} is: {}".format(robot, cost))
    plot_map_circle(problem, routes)


def som(problem, robots, iterations, learning_rate=0.002):
    sigma = 1
    cities = copy.deepcopy(problem)

    # Tạo 1 network ~ con đường ngẫu nhiên của các robot lúc đầu
    network = generate_network(robots, cities)
   
    print("\nNetwork: ")
    print(network)

    normalize(cities)
    print("\nCities: ")
    print(cities)
 
    number_city = len(cities)
    number_robot = len(robots)

    cost = [0] * number_robot
    for i in range(number_robot):
        cost[i] = cal_cost(network[i])
    print("\nCost:")
    print(cost)

    result_network = copy.deepcopy(network)
    max_score = -1

    print('\nNetwork of {} neurons created. Starting the iterations:'.format(len(robots)))

    for i in range(iterations):
        if not i % 100:
            print('\t> Iteration {}/{}'.format(i, iterations), end="\r")
        
        # Permutation các thành phố
        per = list(range(number_city))
        random.shuffle(per)
        for j in range(number_city):
            city = cities[per[j]]

            # Các biến lưu lại giá trị cần thiết của robot có path tốt nhất
            idx_select_robot = -1
            cost_select_robot = -1
            network_select_robot = []
            for robot in range(number_robot):
                tmp_network = adaption(network[robot], city, sigma)
                tmp_cost_robot = cal_cost(tmp_network)
                if cost_select_robot == -1 or cost_select_robot > tmp_cost_robot / robots[robot][0]:
                    cost_select_robot = tmp_cost_robot / robots[robot][0]
                    idx_select_robot = robot
                    network_select_robot = tmp_network
            
            # Điều chỉnh lại con đường cho robot được chọn
            if idx_select_robot != -1 and cost_select_robot < 1:
                network[idx_select_robot] = network_select_robot

        # Loại bỏ các điểm thừa trên mạng qua mỗi epoch
        regeneration(network)

        tmp_score = cal_score(problem, network)  
        if max_score == -1 or max_score < tmp_score:
            max_score = tmp_score
            print("\nMax score is: {}".format(max_score))
            # Lưu lời giải tốt nhất
            result_network = copy.deepcopy(network)

        sigma = sigma * (1 - i * learning_rate)
        if sigma <= 0:
            break
    else:
        print('Completed {} iterations.'.format(iterations))

    return result_network

if __name__ == '__main__':
    main()
