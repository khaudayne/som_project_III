import numpy as np
import math
import copy
import random
from distance import select_closest, find_nearest_way_point, find_nearest_path_point

def generate_network(robots, problem, multi = 2):
    number_robot = len(robots)
    number_waypoint = math.ceil(len(problem) / number_robot)
    network = [[]] * number_robot
    for i in range(number_robot):
        tmp_list = []
        angle = 2 * math.pi / number_waypoint
        radius = problem[i][2] * multi
        for j in range(number_waypoint):
            tmp_list.append([problem[i][0] + radius * math.sin(angle * j), problem[i][1] + radius * math.cos(angle * j)])
        network[i] = tmp_list
    return network

def generate_one_path(network, problem, multi = 2):
    number_robot = len(network)
    number_waypoint = math.ceil(len(problem) / number_robot)
    random_city = random.randint(0, len(problem) - 1)
    gen_network = []
    angle = 2 * math.pi / number_waypoint
    radius = problem[random_city][2] * multi
    for j in range(number_waypoint):
        gen_network.append([problem[random_city][0] + radius * math.sin(angle * j), problem[random_city][1] + radius * math.cos(angle * j)])
    return gen_network


# Param:
## path: network của robot đang xét
## city: thành phố mà robot điều chỉnh hướng . đitoiws
## sigma: tham số điều chỉnh độ kéo của path
### return: network sau khi tuning
def adaption(path, city, sigma):
    tmp_network = copy.deepcopy(path)

    # Tìm way_point nằm trên path gần city nhất
    idx_waypoint, sqr_dis_waypoint, z_nearest_waypoint = find_nearest_way_point(tmp_network, city)

    neareast_point_in_path = None
    idx_insert = None
    z_nearest_path = None
    sqr_dis_point_in_path = -1

    if sqr_dis_waypoint > 0: # Trường hợp không có waypoint nào nằm trong region thì mới xét tới cạnh
        neareast_point_in_path, sqr_dis_point_in_path, idx_insert, z_nearest_path = find_nearest_path_point(tmp_network, city)

        # Trường hợp điểm nằm trên cạnh gần city hơn điểm nằm trên path
        # => Chèn điểm mới vào tmp_network tại idx_insert
        if sqr_dis_point_in_path != -1 and sqr_dis_point_in_path < sqr_dis_waypoint:
            tmp_network.insert(idx_insert, neareast_point_in_path)
            idx_waypoint = idx_insert
            z_nearest_waypoint = z_nearest_path

    # Trong trường hợp z_nearest ở sát biên của đường tròn => Di chuyển lại gần tâm hơn
    z_nearest_waypoint = fix_distance_z_nearest(z_nearest_waypoint, city)
    move_toward(tmp_network, idx_waypoint, z_nearest_waypoint, sigma)
    return tmp_network

def fix_distance_z_nearest(z_nearest, city, threshold = 4 / 5):
    scale = ((z_nearest[0] - city[0]) ** 2 + (z_nearest[1] - city[1]) ** 2) / (city[2] ** 2)
    if(scale <= (threshold ** 2)): 
        return z_nearest
    z_nearest[0] = z_nearest[0] + (city[0] - z_nearest[0]) * (1 - threshold)
    z_nearest[1] = z_nearest[1] + (city[1] - z_nearest[1]) * (1 - threshold)
    return z_nearest
 
def move_toward(path, idx_waypoint, final_z_nearest, sigma):
    sz = len(path)
    for i in range(sz):
        l = min(idx_waypoint - i, sz - idx_waypoint + i)
        factor = function_factor(l, sigma)
        path[i][0] = path[i][0] + (final_z_nearest[0] - path[i][0]) * factor
        path[i][1] = path[i][1] + (final_z_nearest[1] - path[i][1]) * factor

    
def function_factor(l, sigma, landa = 1, multi_factor = 1):
    sqr_sigma = sigma * sigma
    sqr_l = l * l
    if sqr_l == 0:
        return 1
    if sqr_sigma <= 0:
        return 0
    return landa * math.exp(-sqr_l * multi_factor / sqr_sigma)

# todo: thêm hàm để tái tạo đường qua mỗi epoch => Giảm các điểm thừa
def regeneration(network, problem):
    number_city = len(problem)
    check = [False] * number_city
    for i in range(len(network)):
        path = network[i] 
        regeneration_network = []
        for j in range(len(path)):
            for k in range(number_city):
                city = problem[k]
                if check[k]:
                    continue
                if ((path[j][0] - city[0]) ** 2 + (path[j][1] - city[1]) ** 2) <= city[2] ** 2:
                    regeneration_network.append([path[j][0], path[j][1]])
                    check[k] = True

        network[i] = regeneration_network
        if len(network[i]) == 0:
            # Tạo lại 1 đường mới cho robot khi mà đường cũ đã bị xóa hết các điểm
            network[i] = generate_one_path(network, problem)
            pass
    pass


def cal_score(problem, network):
    check = [False] * len(problem)
    for i in range(len(network)):
        for j in range(len(network[i])):
            way_point = network[i][j]
            for k in range(len(problem)):
                if check[k]:
                    continue

                #kiểm tra way_point có nằm trong region view_point của điểm cần quan sát hay không
                sqr_dis = (way_point[0] - problem[k][0]) ** 2 + (way_point[1] - problem[k][1]) ** 2
                if sqr_dis <= problem[k][2] * problem[k][2]:
                    check[k] = True
    
    score = 0
    for i in range(len(problem)):
        if check[i]:
            score += problem[k][3]
    return score