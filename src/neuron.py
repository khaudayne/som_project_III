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
        angle = math.pi / number_waypoint
        radius = problem[i][2] * multi
        for j in range(number_waypoint):
            tmp_list.append(
                [
                    problem[i][0] + radius * math.sin(angle * j)
                    , problem[i][1] + radius * math.cos(angle * j)
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

# Param:
## path: network của robot đang xét
## city: thành phố mà robot điều chỉnh hướng . đitoiws
## sigma: tham số điều chỉnh độ kéo của path
### return: network sau khi tuning
def adaption(path, city, sigma):
    tmp_network = copy.deepcopy(path)

    # Tìm way_point nằm trên path gần city nhất
    idx_waypoint, sqr_dis_waypoint, z_nearest_waypoint = find_nearest_way_point(tmp_network, city)

    final_waypoint = tmp_network[idx_waypoint]
    final_z_nearest = z_nearest_waypoint

    neareast_point_in_path = None
    idx_insert = None
    z_nearest_path = None
    sqr_dis_point_in_path = 2 # Đặt là 2 vì map được normalize về [0; 1]

    if sqr_dis_waypoint > 0: # Trường hợp không có waypoint nào nằm trong region thì mới xét tới cạnh
        neareast_point_in_path, sqr_dis_point_in_path, idx_insert, z_nearest_path = find_nearest_path_point(tmp_network, city)

        # Trường hợp điểm nằm trên cạnh gần city hơn điểm nằm trên path
        # => Chèn điểm mới vào tmp_network tại idx_insert
        if sqr_dis_point_in_path < sqr_dis_waypoint:
            tmp_network.insert(idx_insert, neareast_point_in_path)
            final_waypoint = neareast_point_in_path
            final_z_nearest = z_nearest_path

    for i in range(len(tmp_network)):
        move_toward(tmp_network[i], final_waypoint, final_z_nearest, sigma)
    return tmp_network

def move_toward(point, final_waypoint, final_z_nearest, sigma):
    sqr_l = (final_waypoint[0] - point[0]) ** 2 + (final_waypoint[1] - point[1]) ** 2
    f_factor = function_factor(sqr_l, sigma)
    point[0] = point[0] + f_factor * (final_z_nearest[0] - point[0])
    point[1] = point[1] + f_factor * (final_z_nearest[1] - point[1])

    
def function_factor(sqr_l, sigma, landa = 1):
    sqr_sigma = sigma ** 2
    if sqr_sigma <= 0:
        return 0
    return landa * math.exp(-sqr_l / sqr_sigma)

# todo: thêm hàm để tái tạo đường qua mỗi epoch => Giảm các điểm thừa
def regeneration(network):
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
                dis = (way_point[0] - problem[k][0])  * (way_point[0] - problem[k][0]) 
                + (way_point[1] - problem[k][1]) * (way_point[1] - problem[k][1])
                if dis * dis <= problem[k][2] * problem[k][2]:
                    check[k] = True
    
    score = 0
    for i in range(len(problem)):
        if check[i]:
            score += problem[k][3]
    return score