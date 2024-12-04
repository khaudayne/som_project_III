import numpy as np
from sklearn.cluster import KMeans


# Danh sách 2x3
lst = [[1, 2, 3], [10.5, 11.123, 6], [2, 1, 0], [11, 12, 5], [3, 2, 0], [-1, 0 ,0]]

# Chuyển list thành numpy array và lấy 2 cột đầu
array_2x2 = np.array(lst)[:, :2]
print("Array 2x2:")
print(array_2x2)

# Khởi tạo mô hình KMeans với 2 cụm
kmeans = KMeans(n_clusters=2, random_state=0)

# Huấn luyện mô hình trên array 2x2
kmeans.fit(array_2x2)

l = kmeans.cluster_centers_
for i in range(len(l)):
    print("CENTER IS: {} and {}".format(l[i][0], l[i][1]))