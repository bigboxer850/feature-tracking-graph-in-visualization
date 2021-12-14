import pickle

pickel_in = open("NestedTrackingGraph.pickel","rb")
graph = pickle.load(pickel_in)
pickel_in.close()
nodes=graph["nodes"]
nestingEdges=graph["nestingEdges"]

# for node in nodes:
#     if (node.find('l1') != -1):
        # print(node)

trackingEdges=graph["trackingEdges"]

#for tEdge in trackingEdges:
#     print(tEdge[1])
# for nEdge in nestingEdges:
#     if (nEdge[0].find('4') != -1 and nEdge[0].find('t41') != -1):
#         if (nEdge[1].find('4') != -1 and nEdge[1].find('t41') != -1):
#             print(nEdge)

for nEdge in nestingEdges:
        print(nEdge)