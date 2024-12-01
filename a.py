import pandas as pd

# Dữ liệu mới
data = [
    "14.2886061668396/45/291.0/2005.8212112176707",
    "12.20150351524353/44/262.0/1929.209084853726",
    "13.189382791519165/41/257.0/1987.2690801161457",
    "11.9634850025177/45/264.0/1989.503921633275",
    "14.952906608581543/45/289.0/1994.7177751641048",
    "13.166759490966797/44/259.0/1995.8031328152622",
    "14.043452262878418/43/257.0/1997.5189003120977",
    "15.145601272583008/49/308.0/2009.3215027110296",
    "14.914262533187866/47/293.0/1995.085913835733",
    "14.486065864562988/45/292.0/1990.2285658789096"
]

# Chuyển dữ liệu thành một dataframe
# Tách từng chuỗi bằng dấu "/"
data_split = [line.split("/") for line in data]

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data_split, columns=["Column 1", "Column 2", "Column 3", "Column 4"])

# Chuyển các cột cần tính toán thành kiểu dữ liệu số (float)
df["Column 1"] = df["Column 1"].astype(float)
df["Column 2"] = df["Column 2"].astype(float)
df["Column 3"] = df["Column 3"].astype(float)
df["Column 4"] = df["Column 4"].astype(float)

# Tính min, max, và trung bình của từng cột
min_values = df.min()
max_values = df.max()
mean_values = df.mean()

# In kết quả theo định dạng yêu cầu
for i in range(1, 5):
    print(f"Cột {i}: min {min_values[f'Column {i}']:.15f} max {max_values[f'Column {i}']:.15f} trung bình {mean_values[f'Column {i}']:.15f}")
