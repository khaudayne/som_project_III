import random
MIN_POS = 20
MAX_POS = 980
MAX_RADIUS = 15
MIN_RADIUS = 5
MAX_SIZE = 1000
filename = "assets/circles.txt"
with open(filename, "w") as file:
    for _ in range(10):
        x = round(random.uniform(MIN_POS, MAX_POS), 4)
        y = round(random.uniform(MIN_POS, MAX_POS), 4)
        r = round(random.uniform(MIN_RADIUS, MAX_RADIUS), 4)
        file.write(f"{_ + 1} {x} {y} {r}\n")