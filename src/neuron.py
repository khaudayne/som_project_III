import numpy as np

from distance import select_closest

def generate_network(size):
    return np.random.rand(size, 2)

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