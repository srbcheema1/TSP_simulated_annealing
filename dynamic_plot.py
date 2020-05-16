import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time

class DynamicPlot():
	def __init__(self):
		plt.ion() # plot interactive mode ON
		self.figure, self.ax = plt.subplots(2,2)
		self.cyan_line, = self.ax[0,0].plot([],[], 'co-') # intermediate path
		self.green_line, = self.ax[0,0].plot([],[], 'go-') # final path
		self.red_line, = self.ax[0,0].plot([],[], 'ro') # depot
		self.ax[0,0].set_title("Simulated Annealing")
		self.ax[1,1].set_title("Optmimization")

	def plot(self, cities, path: list):
		x = []
		y = []

		path.append(path[0])
		for index in range(0, len(path)):
			city = cities[path[index]]
			x.append(city.x)
			y.append(city.y)
		
		self.cyan_line.set_data(x, y)
		self.red_line.set_data([cities[0].x],[cities[0].y])

		self.ax[0,0].set_xlim(0, (max(x)+2) * 1.1)
		self.ax[0,0].set_ylim(0, (max(y)+2)* 1.1)
		self._flush()
	
	def plot_final(self,cities,path:list):
		x = []
		y = []

		path.append(path[0])
		for index in range(0, len(path)):
			city = cities[path[index]]
			x.append(city.x)
			y.append(city.y)
		
		self.cyan_line.set_data([], [])
		self.green_line.set_data(x,y)
		self.red_line.set_data([cities[0].x],[cities[0].y])

		self.ax[0,0].set_xlim(0, (max(x)+2) * 1.1)
		self.ax[0,0].set_ylim(0, (max(y)+2)* 1.1)
		self._flush()

	def plot_mst(self,graph):
		lines = graph.minimumSpanningTree()[1]
		c = [(1,0,0,1) for i in range(len(lines))]
		lc = mc.LineCollection(lines, colors=c, linewidths=3)
		self.ax[0,0].add_collection(lc)

	def show(self,cities,history,graph):
		for path in history[:-1]:
			self.plot(cities,path)
			time.sleep(1)
		self.plot_final(cities,history[-1])
		self.plot_mst(graph)
		self.plot_learning(history,graph)
		self.end()

	def end(self):
		plt.ioff()
		plt.show()
	
	def plot_learning(self,history,graph):
		self.ax[1,1].plot([i for i in range(len(history))], [graph.path_cost(i) for i in history])
		line_init = self.ax[1,1].axhline(y=graph.path_cost(history[0]), color='y', linestyle='--')
		line_min = self.ax[1,1].axhline(y=graph.path_cost(history[-1]), color='g', linestyle='--')
		line_mst = self.ax[1,1].axhline(y=graph.minimumSpanningTree()[0], color='b', linestyle='--')
		line_mst2 = self.ax[1,1].axhline(y=graph.minimumSpanningTree()[0]*2, color='r', linestyle='--')
		self.ax[1,1].legend([line_init, line_min, line_mst,line_mst2], 
					['NNA cost', 'SA cost','mst cost lower','2 * mst cost'])
		self.ax[1,1].set(xlabel='iteration', ylabel='cost')

	def _flush(self):
		#We need to draw *and* flush0
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()