import random
import numpy as np
MIN_POS = 20
MAX_POS = 980
MAX_RADIUS = 35
MIN_RADIUS = 20
MAX_SIZE = 1000
MAX_REWARD = 4
MIN_REWARD = 1
filename = "assets/circles.txt"
def create_circle_uniform(number_city):
    with open(filename, "w") as file:
        for _ in range(number_city):
            x = round(random.uniform(MIN_POS, MAX_POS), 4)
            y = round(random.uniform(MIN_POS, MAX_POS), 4)
            r = round(random.uniform(MIN_RADIUS, MAX_RADIUS), 4)
            reward = random.randint(MIN_REWARD, MAX_REWARD)
            file.write(f"{_ + 1} {x} {y} {r} {reward}\n")

def create_circle_gauss(number_city):
    mean = MAX_SIZE / 2  
    std_dev = MAX_SIZE / 6 
    x_coords = np.random.normal(mean, std_dev, number_city)
    y_coords = np.random.normal(mean, std_dev, number_city)
    with open(filename, "w") as file:
        for i in range(number_city):
            x = round(x_coords[i], 4)
            y = round(y_coords[i], 4)
            r = round(random.uniform(MIN_RADIUS, MAX_RADIUS), 4)
            reward = random.randint(MIN_REWARD, MAX_REWARD)
            file.write(f"{i + 1} {x} {y} {r} {reward}\n")
create_circle_gauss(500)

