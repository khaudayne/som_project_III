import matplotlib.pyplot as plt
import numpy as np

x = [20, 30, 40, 50]
sp = ("2 robots", "3 robots", "4 robots", "5 robots")
list_cost_after = [
    [175.0, 58.0],
    [118.0, 70.0, 45.0],
    [80.0, 60.0, 56.0, 37.0],
    [63.0, 55.0, 56.0, 37.0, 22.0]
]
list_cost_before = [
    [172.0, 61.0],
    [93.0, 62.0, 78.0],
    [39.0, 62.0, 78.0, 54.0],
    [41.0, 61.0, 58.0, 47.0, 26.0]
]
cost_all_robot_after = [
    233.0,
    233.0,
    233.0,
    233.0
]
cost_all_robot_before = [
    233.0,
    233.0,
    233.0,
    233.0
]

# Tạo figure và trục đầu tiên
fig, ax1 = plt.subplots()

# Vẽ đồ thị đầu tiên (trục Y bên trái)
for i in range(4):
    start_x = x[i]
    data_after = list_cost_after[i]
    data_before = list_cost_before[i]
    sz = len(data_after)
    number_robot = sz * 2
    offset_w = (number_robot - 1) / 2
    x_tmp = np.arange(start_x, start_x + number_robot) - offset_w
    for j in range(sz):
        bar = ax1.bar(x_tmp[j], data_after[j], 1, color="orange", edgecolor= 'black')
        if i == 0 and j == 0:
            bar.set_label("reward after one robot")
    for j in range(sz):
        bar = ax1.bar(x_tmp[j + sz], data_before[j], 1, color="lime", edgecolor= 'black')
        if i == 0 and j == 0:
            bar.set_label("reward before one robot")
ax1.plot(x, cost_all_robot_after, color='blue', label='reward after all robot')
ax1.plot(x, cost_all_robot_before, color='green', label='reward before all robot')

ax1.set_ylabel("Reward")  # Nhãn cho trục Y (bên trái)
ax1.set_ylim(0,270)
ax1.set_xlabel("Number of robots")
ax1.set_xticks(x, sp)
ax1.legend(loc='upper left', ncols = 2)
plt.title("Case high budget in map this has 100 goals")
plt.show()
