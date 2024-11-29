import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import create_circle
import numpy as np

LIST_COLOR = ["#011F82", "#00BAF7", "#D97903"]
COLOR_CIRCLE = "green"
COLOR_CIRCLE_UNVISIT = "red"
COLOR_POINT_CIRCLE = "red"
def plot_network(cities, neurons, name='diagram.png', ax=None):
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        axis.scatter(cities['x'], cities['y'], color='red', s=4)
        axis.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(cities['x'], cities['y'], color='red', s=4)
        ax.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)
        return ax

def plot_route(cities, route, name='diagram.png', ax=None):
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        axis.scatter(cities['x'], cities['y'], color='red', s=4)
        route = cities.reindex(route)
        route.loc[route.shape[0]] = route.iloc[0]
        axis.plot(route['x'], route['y'], color='purple', linewidth=1)

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(cities['x'], cities['y'], color='red', s=4)
        route = cities.reindex(route)
        route.loc[route.shape[0]] = route.iloc[0]
        ax.plot(route['x'], route['y'], color='purple', linewidth=1)
        return ax

def plot_map_circle(cities, routes, list_check, name="diagrams/map_circle.jpg"):
    mpl.rcParams['agg.path.chunksize'] = 10000
    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])
    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    # Normalize về [0; 1) để vẽ hình
    for i in range(len(cities)):
        cities[i][0] /= create_circle.MAX_SIZE
        cities[i][1] /= create_circle.MAX_SIZE
        cities[i][2] /= create_circle.MAX_SIZE

    for i in range(len(routes)):
        for j in range(len(routes[i])):
            routes[i][j][0] /= create_circle.MAX_SIZE
            routes[i][j][1] /= create_circle.MAX_SIZE

    # Vẽ các region city
    idx = 0
    for circle in cities:
        if list_check[idx]:
            c = patches.Circle((circle[0], circle[1]), circle[2], edgecolor=COLOR_CIRCLE, facecolor='none', linewidth=1)
        else:
            c = patches.Circle((circle[0], circle[1]), circle[2], edgecolor=COLOR_CIRCLE_UNVISIT, facecolor='none', linewidth=1)
        axis.scatter(circle[0], circle[1], color=COLOR_POINT_CIRCLE, zorder=5, s=1)
        axis.add_patch(c)
        idx = idx + 1
    
    # todo : ve them cac diem waypoint cua robot
    for i in range(len(routes)):
        for j in range(len(routes[i])):
            axis.scatter(routes[i][j][0], routes[i][j][1], color=LIST_COLOR[i], zorder=5, s=4)

    # Vẽ path của các con robot
    for i in range(len(routes)):
        if len(routes[i]) <= 1:
            continue
        tmp_first_element = [routes[i][0][0], routes[i][0][1]]
        routes[i].append(tmp_first_element)
        tmp_arr = np.array(routes[i])
        axis.plot(tmp_arr[:,0], tmp_arr[:,1], 'r.', ls='-', color=LIST_COLOR[i], markersize=2)

    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()