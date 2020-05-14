from simulated_annealing import SimulatedAnnealing
from city import City
from graph import Graph
from dynamic_plot import DynamicPlot


def main():
    '''set the simulated annealing algorithm params'''
    temp = 10
    stopping_temp = 0.00000001
    alpha = 0.9998
    stopping_iter = 1000000000

    '''set the dimensions of the grid'''
    size_width = 100
    size_height = 100

    '''set the number of nodes'''
    population_size = 120

    '''generate random list of nodes'''
    cities = City.load_cities('./data/data1.txt')
    graph = Graph(cities)

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(graph, temp, alpha, stopping_temp, stopping_iter)
    history = sa.anneal()
    print(len(history))
    DynamicPlot().show(cities,history)

if __name__ == "__main__":
    main()
