from simulated_annealing import SimulatedAnnealing
from city import City
from graph import Graph
from dynamic_plot import DynamicPlot


def main():
    cities = City.load_cities('./data/data1.txt')
    graph = Graph(cities)
    init_sol = graph.nearestNeighbourSolution()

    history = SimulatedAnnealing(graph, init_sol, 0.9998, 10, 0.0000001, 1000000).anneal()
    DynamicPlot().show(cities,history)

if __name__ == "__main__":
    main()
