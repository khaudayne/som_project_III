import statistics
l1 = []
l2 = []
l3 = []

# Đọc dữ liệu từ file origin.txt
with open("report/log_100/hb_mix.txt", "r") as file:
    data = file.readlines()
    for line in data:
        tmp = list(map(float, line.strip().split()))
        l1.append(tmp[0])
        l2.append(tmp[1])
        l3.append(tmp[2])

# In kết quả
mean = []
std_dev = []

mean.append(statistics.mean(l1))
mean.append(statistics.mean(l2))
mean.append(statistics.mean(l3))

std_dev.append(statistics.stdev(l1))
std_dev.append(statistics.stdev(l2))
std_dev.append(statistics.stdev(l3))

print(mean)
print(std_dev)

