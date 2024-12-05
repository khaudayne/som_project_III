import random
MIN_POS = 20
MAX_POS = 980
MAX_RADIUS = 35
MIN_RADIUS = 20
MAX_SIZE = 1000
MAX_REWARD = 4
MIN_REWARD = 1
filename = "assets/circles.txt"
with open(filename, "w") as file:
    for _ in range(10):
        x = round(random.uniform(MIN_POS, MAX_POS), 4)
        y = round(random.uniform(MIN_POS, MAX_POS), 4)
        r = round(random.uniform(MIN_RADIUS, MAX_RADIUS), 4)
        reward = random.randint(MIN_REWARD, MAX_REWARD)
        file.write(f"{_ + 1} {x} {y} {r} {reward}\n")