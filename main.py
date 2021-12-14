import pickle
import EdgesGenerator as EG
import NodesGenerator as NG
import sys
sys.setrecursionlimit(3000)

def main():
    Graph = {}
    # Graph['nodes'] = NG.generateNodes()
    #Graph['nestingEdges'] = EG.createNestedTrees()
    Graph['trackingEdges'] = EG.createTrackingTree()
    # print(Graph)
    pickle_out = open("NestedTrackingGraph.pickel","wb")
    pickle.dump(Graph, pickle_out)
    pickle_out.close()

main()