import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def animateTSP(history, cities):
    ''' animate the solution over time
        hisotry : list;history of the solutions chosen by the algorithm
        cities: array_like, cities with the coordinates
    '''

    ''' approx 1500 frames for animation '''
    key_frames_mult = len(history) // 5000

    fig, ax = plt.subplots()
    line, = plt.plot([], [], lw=2)

    def init():
        ''' initialize node dots on graph '''
        x = [cities[i].x for i in history[0]]
        y = [cities[i].y for i in history[0]]
        plt.plot(x, y, 'co')

        ''' draw axes slighty bigger  '''
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        '''initialize solution to be empty '''
        line.set_data([], [])
        return line,

    def update(frame):
        ''' for every frame update the solution on the graph '''
        x = [cities[i].x for i in history[frame] + [history[frame][0]]]
        y = [cities[i].y  for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line

    ''' animate precalulated solutions '''
    ani = FuncAnimation(fig, update, frames=range(0, len(history), key_frames_mult), init_func=init, interval=3, repeat=False)
    plt.show()