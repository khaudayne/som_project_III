from sys import argv

import numpy as np
import copy
import random
from io_helper import read_tsp, normalize
from neuron import generate_network, adaption, regeneration, cal_score, get_list_check_city
from distance import cal_cost
from plot import plot_map_circle
import time

MAX_EPOCH = 50
MAX_COST = 10000000000
def main(name_problem, after_name = ""):
    problem, robots = read_tsp("assets/" + name_problem + ".tsp")

    print("\nRobots: ")
    print(robots)

    print("\Problem: ")
    print(problem)

    start_time = time.time()
    routes = som(problem, robots, 100000)
    end_time = time.time()
    print("\nRoutes: ")
    print(routes)

    time_run_alg = end_time - start_time

    total_cost_robot = 0
    for robot in range(len(routes)):
        cost = cal_cost(routes[robot])
        total_cost_robot = total_cost_robot + cost
        print("Cost of robot {} is: {}".format(robot, cost))

    list_check = get_list_check_city(problem, routes)
    number_city_visited = 0
    total_score = 0
    for i in range(len(list_check)):
        if list_check[i]:
            total_score = total_score + problem[i][3]
            number_city_visited = number_city_visited + 1

    # WRITE LOG AS: TIME_RUN / NUMBER_CITY_VISITED / TOTAL_SCORE / TOTAL_COST_ROBOT
    with open("report/log_metric/" + name_problem + "_" + after_name + ".txt", "a") as f:
        f.write("\n{}/{}/{}/{}".format(time_run_alg, number_city_visited, total_score, total_cost_robot))

    plot_map_circle(problem, routes, list_check, "report/img_report/" + name_problem + "_" + after_name + ".jpg")

def som(problem, robots, iterations, learning_rate=0.002):
    sigma = 1
    cities = copy.deepcopy(problem)

    # Tạo 1 network ~ con đường ngẫu nhiên của các robot lúc đầu
    network = generate_network(robots, cities)
   
    print("\nNetwork: ")
    print(network)

    normalize(cities)
 
    number_city = len(cities)
    number_robot = len(robots)

    cost = [0] * number_robot
    for i in range(number_robot):
        cost[i] = cal_cost(network[i])
    print("\nCost:")
    print(cost)

    result_network = copy.deepcopy(network)
    max_score = -1

    count_epoch_none_incre = 0
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
            cost_select_robot = MAX_COST
            network_select_robot = []
            for robot in range(number_robot):
                tmp_network = adaption(network[robot], city, sigma)
                tmp_cost_robot = cal_cost(tmp_network) - cal_cost(network[robot])
                # Thay đổi hàm để chọn robot
                ## => Ưu tiên các con robot có sự thay đổi năng lượng ít hơn?
                if cost_select_robot > tmp_cost_robot:
                    cost_select_robot = tmp_cost_robot
                    idx_select_robot = robot
                    network_select_robot = tmp_network
            
            # Điều chỉnh lại con đường cho robot được chọn
            if idx_select_robot != -1 and (cal_cost(network_select_robot) <= robots[idx_select_robot][0]):
                network[idx_select_robot] = network_select_robot

        # Loại bỏ các điểm thừa trên mạng qua mỗi epoch
        regeneration(network, problem)

        tmp_score = cal_score(problem, network)  
        if max_score == -1 or max_score < tmp_score:
            max_score = tmp_score
            print("\nMax score is: {}".format(max_score))
            # Lưu lời giải tốt nhất
            result_network = copy.deepcopy(network)
            count_epoch_none_incre = 0
        else:
            count_epoch_none_incre += 1

        if count_epoch_none_incre >= MAX_EPOCH:
            break
        sigma = sigma * (1 - i * learning_rate)
        if sigma <= 0:
            break
    else:
        print('Completed {} iterations.'.format(iterations))

    return result_network

# if __name__ == '__main__':
#     main()
main("map_3_150_hb", "after")