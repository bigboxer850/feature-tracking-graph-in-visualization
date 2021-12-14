import networkx as nx
def get_tracking(v1, v2, edges):
	G = nx.Graph()
	G.add_nodes_from(v1, bipartite = 0)
	G.add_nodes_from(v2, bipartite = 1)
	for e in edges:
		G.add_edge(e[0], e[1], weight = e[2])
	# print(G.adj)
	matching = nx.algorithms.matching.max_weight_matching(G, weight = 'weight')
	print(len(matching))

	# findind new relation using merge and split
	vis1 = set()
	vis2 = set()
	for m in matching:
		u = min(m[0], m[1])
		v = max(m[0], m[1])
		print(u, v)
		vis1.add(u)
		vis2.add(v)
	print()
	print("++++++++++++++++++++++++++++++++++")
	print()

	for e in edges:
		u = min(e[0], e[1])
		v = max(e[0], e[1])
		if u in vis1 and v in vis2:
			continue
		vis1.add(u)
		vis2.add(v)
		print(u, v)
		matching.add((u, v))

	# print(len(matching))


	
		
