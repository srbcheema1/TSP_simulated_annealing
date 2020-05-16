from .blossom import srb_blossom

def christofied_optimization(graph):
  mst_cost,_,parent = graph.minimumSpanningTree()
  node_degree = [1 for i in range(graph.size)]
  for val in parent:
    if(val == -1):
      continue
    node_degree[val] +=1
  
  odd_nodes = []
  for i in range(graph.size):
    if(node_degree[i]%2==1):
      odd_nodes.append(i)

  blossom_edges = []
  for i,a in enumerate(odd_nodes):
    for j,b in enumerate(odd_nodes):
      if(a==b):
        continue
      blossom_edges.append([i,j,graph.cost[a][b]])
  
  # covering_cost = srb_blossom(blossom_edges)[0] # this was taking a lot of time
  edge_weights = [a[2] for a in blossom_edges]
  edge_weights.sort()
  covering_cost = sum(edge_weights[:len(odd_nodes)//2])
  return max(mst_cost,(mst_cost + covering_cost)*2/3)