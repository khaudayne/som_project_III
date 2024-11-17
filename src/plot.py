import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import create_circle
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

def plot_map_circle(cities, name="diagrams/map_circle.png"):
    mpl.rcParams['agg.path.chunksize'] = 10000
    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])
    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    for circle in cities:
        c = patches.Circle((circle[0], circle[1]), circle[2], edgecolor='blue', facecolor='none', linewidth=1)
        axis.scatter(circle[0], circle[1], color='red', zorder=5, s=1)
        axis.add_patch(c)

    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()