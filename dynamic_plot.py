import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time

class DynamicPlot():
	def __init__(self):
		plt.ion() # plot interactive mode ON
		self.figure, self.ax = plt.subplots(2,2)
		self.cyan_line, = self.ax[1,0].plot([],[], 'co-') # intermediate path
		self.green_line, = self.ax[1,0].plot([],[], 'go-') # final path
		self.red_line, = self.ax[1,0].plot([],[], 'ro') # depot
		self.ax[0,0].set_title("Nearest Neighbour Algorithm")
		self.ax[0,1].set_title("Minimum Spanning Tree")
		self.ax[1,0].set_title("Simulated Annealing")
		self.ax[1,1].set_title("Optmimization")

	def get_xy(self,cities,p_path:list):
		x, y = [], []
		path = p_path[:]
		path.append(path[0])
		for index in range(0, len(path)):
			city = cities[path[index]]
			x.append(city.x)
			y.append(city.y)
		return x,y

	def set_lim(self,x0,x1,y0,y1,ax):
		ax.set_xlim(x0, x1)
		ax.set_ylim(y0, y1)

	def plot(self, cities, path: list):
		x,y = self.get_xy(cities,path)
		self.cyan_line.set_data(x, y)
		self.red_line.set_data([cities[0].x],[cities[0].y])
		self._flush()
	
	def plot_final(self,cities,path:list):
		x,y = self.get_xy(cities,path)
		self.cyan_line.set_data([], [])
		self.green_line.set_data(x,y)
		self.red_line.set_data([cities[0].x],[cities[0].y])
		self._flush()

	def plot_mst(self,graph,x,y,cities):
		lines = graph.minimumSpanningTree()[1]
		c = [(0,0,1,1) for i in range(len(lines))]
		lc = mc.LineCollection(lines, colors=c, linewidths=1)
		self.ax[0,1].add_collection(lc)
		self.ax[0,1].plot(x,y, 'bo')
		self.ax[0,1].plot([cities[0].x],[cities[0].y],'ro')

	def plot_nna(self,x,y,cities):
		self.ax[0,0].plot(x,y, 'yo-')
		self.ax[0,0].plot([cities[0].x],[cities[0].y],'ro')

	def show(self,cities,history,graph):
		x,y = self.get_xy(cities,history[0])
		self.set_lim(0, (max(x)+2) * 1.1, 0, (max(y)+2)* 1.1,self.ax[0,0])
		self.set_lim(0, (max(x)+2) * 1.1, 0, (max(y)+2)* 1.1,self.ax[0,1])
		self.set_lim(0, (max(x)+2) * 1.1, 0, (max(y)+2)* 1.1,self.ax[1,0])

		self.plot_nna(x,y,cities)
		self.plot_mst(graph,x,y,cities)
		for path in history[:-1]:
			self.plot(cities,path)
			time.sleep(1)
		self.plot_final(cities,history[-1])
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
		self.ax[1,1].legend([line_mst2,line_init, line_min, line_mst], 
					['2 * mst','NNA cost', 'SA cost','mst cost'])
		self.ax[1,1].set(xlabel='iteration', ylabel='cost')

	def _flush(self):
		#We need to draw *and* flush0
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()