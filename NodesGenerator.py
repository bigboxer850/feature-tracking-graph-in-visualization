import pickle
import FloodFill as FF
import meshio

xd = FF.xd
yd = FF.yd
zd = FF.zd
levels = [0.5] #level1 = levels[0]

inputpath = "./VTK_dataset/"
outputpath = "./nodes/"
filePrefix = "SquareCylinderOkuboWeiss_t_"
inputFormat = ".vtk"



def generateNodes():
    graph_nodes = []
    for timestep in range(33, 35):#509
        fileName = inputpath + filePrefix + str(timestep) + inputFormat
        mesh = meshio.read(fileName)
        magnitude = (mesh.point_data['magnitude']).flatten()
        nodes_in_timestep = {}
        for index in range(len(levels)):
            level = levels[index]
            compNo1 = (magnitude<level) * -1
            compNo2 = (magnitude>=level) * -2
            compNo = compNo2 + compNo1
            id = 0
            nodes_in_level = []
            for i in range(xd):
                for j in range(yd):
                    for k in range(zd):
                        if(compNo[((k * yd + j) * xd + i)]==-2):
                            id += 1
                            (newNode, compNo) = FF.floodfill(i,j,k,level,id,compNo)
                            nodes_in_level.append(newNode)
                            graph_nodes.append("t"+str(timestep)+"_l"+str(index+1)+"_"+str(id))
            nodes_in_timestep["timestep"+str(timestep)] =  nodes_in_level
            nodes_in_timestep["volume"] =  compNo
            a=set(compNo)
            print(a)

        print(nodes_in_timestep)
        
        outputFile = outputpath+"nodes_t"+str(timestep)+".pickle"
        pickle_out = open(outputFile,"wb")
        pickle.dump(nodes_in_timestep, pickle_out)
        pickle_out.close()

    return graph_nodes
    
        # print(nodes_in_timestep)

