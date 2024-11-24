import numpy as np
import math

def select_closest(candidates, origin):
    return euclidean_distance(candidates, origin).argmin()

def euclidean_distance(a, b):
    return np.linalg.norm(a - b, axis=1)

def route_distance(cities):
    points = cities[['x', 'y']]
    # Roll các phần tử lên 1 để tính khoảng cách giữa dãy điểm liên tiếp
    distances = euclidean_distance(points, np.roll(points, 1, axis=0))
    return np.sum(distances)

def cal_cost(path):
    c = 0
    for i in range(len(path)):
        c += math.sqrt(
            (path[i][0] - path[i - 1][0]) * (path[i][0] - path[i - 1][0]) 
            + (path[i][1] - path[i - 1][1]) * (path[i][1] - path[i - 1][1])
        )
    return c

def find_point_nearest_in_circle(point, circle):
    dis = math.sqrt((point[0] - circle[0])  * (point[0] - circle[0]) 
        + (point[1] - circle[1]) * (point[1] - circle[1]))
    scale = (dis - circle[2]) / dis
    return [point[0] + scale * (circle[0] - point[0]), point[1] + scale * (circle[1] - point[1])]

# Hàm trả về waypoint nằm trên network gần tâm của city nhất, nếu nằm
# trong region của city thì khoảng cách được xét là 0
## return: idx của waypoint gần nhất và sqr_distance của waypoint tới city       
def find_nearest_way_point(network, city):
    sqr_radius = city[2] * city[2]
    min_dis = -1
    min_idx = -1
    for i in range(len(network)):
        way_point = network[i]
        dis = (way_point[0] - city[0])  * (way_point[0] - city[0]) 
        + (way_point[1] - city[1]) * (way_point[1] - city[1])
        
        dis = max(dis - sqr_radius, 0)
        if min_dis == -1 or min_dis > dis:
            min_dis = dis
            min_idx = i
        
        # Trường hợp có 1 điểm trên đường nằm trong region thì trả về luôn
        if min_dis <= 0:
            return min_idx, 0, [network[min_idx][0], network[min_idx][1]]
    z_nearest = find_point_nearest_in_circle(network[min_idx], city)
    return min_idx, min_dis, z_nearest

# Tác dụng giống hàm find_nearest_way_point nhưng tìm điểm nằm trên cạnh
def find_nearest_path_point(network, city):
    sqr_radius = city[2] * city[2]
    xt_min = -1
    yt_min = -1
    idx_insert = -1
    min_dis = -1 
    for i in range(len(network)):
        A = network[i]
        B = network[i - 1]
        if B[0] == A[0] and B[1] == A[1]:
            continue
        t = - ((B[0] - A[0]) * (A[0]- city[0]) + (B[1] - A[1]) * (A[1]- city[1])) / ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
        if t < 0 or t > 1:
            continue
        xt_tmp = A[0] + t * (B[0] - A[0])
        yt_tmp = A[1] + t * (B[1] - A[1])
        dis = (xt_tmp - city[0]) ** 2 + (yt_tmp - city[1]) ** 2
        dis = max(dis - sqr_radius, 0)

        if min_dis == -1 or min_dis > dis:
            min_dis = dis
            xt_min = xt_tmp
            yt_min = yt_tmp
            idx_insert = i
        
        # Trường hợp điểm nằm trên path cũng nằm trong region thì return luôn
        if min_dis <= 0 and idx_insert >= 0:
            return [xt_min, yt_min], 0, idx_insert, [xt_min, yt_min]
        
    # Trường hợp tệ, tất cả các điểm gần nhất đều nằm ngoài đoạn thẳng
    if xt_min < 0 or yt_min < 0 or min_dis < 0 or idx_insert < 0:
        return None, -1, None, None
    z_nearest = find_point_nearest_in_circle([xt_min, yt_min], city)
    return [xt_min, yt_min], min_dis, idx_insert, z_nearest
