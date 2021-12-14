import pickle
import two_step_optimization as T
xd = 192
yd = 64
zd = 48
inputpath = "./nodes/"

EG = [
('501_32', '502_47', 0.008869179600886918),
('501_19', '502_29', 0.652542372881356),
('501_2', '502_6', 0.00040112314480545525),
('501_4', '502_7', 0.0005518763796909492),
('501_5', '502_10', 0.07894736842105263),
('501_21', '502_27', 0.5492424242424242),
('501_3', '502_2', 0.4126869706253379),
('501_13', '502_18', 0.4891304347826087),
('501_4', '502_21', 0.06098233995584989),
('501_7', '502_12', 0.2),
('501_4', '502_9', 0.42328918322295805),
('501_14', '502_19', 0.4157303370786517),
('501_22', '502_30', 0.24675324675324675),
('501_4', '502_20', 0.0576710816777042),
('501_16', '502_24', 0.588),
('501_2', '502_5', 0.0008022462896109105),
('501_20', '502_26', 0.5406871609403255),
('501_3', '502_4', 0.0003508771929824561),
('501_23', '502_37', 0.58994708994709),
('501_18', '502_28', 0.6607142857142857),
('501_25', '502_39', 0.5606060606060606),
('501_33', '502_50', 0.75),
('501_32', '502_46', 0.5432372505543237),
('501_36', '502_49', 0.75),
('501_4', '502_8', 0.0002759381898454746),
('501_35', '502_48', 0.9619047619047619),
('501_6', '502_11', 0.11904761904761904),
('501_1', '502_1', 0.9750499001996008),
('501_2', '502_2', 0.4352135519913498),
('501_17', '502_25', 0.5887096774193549),
('501_24', '502_38', 0.6176470588235294)
]

def weigh(volume_t1,volume_t2,x,y):
    volume_1=list(volume_t1)
    volume_2=list(volume_t2)
    big_volume=max(volume_1.count(x),volume_2.count(y))
    count=0
    for i in range(xd):
        for j in range(yd):
            for k in range(zd):
                if(volume_t1[((k * yd + j) * xd + i)]==x and volume_t2[((k * yd + j) * xd + i)]==y):
                    count=count+1
    return count/big_volume          
def connectedComponents(volume_t1, volume_t2,a,b,first,second):
    edges = set()
    for i in a:
        for j in b:
            weight=weigh(volume_t1,volume_t2,i,j)
            if(weight>0):
                edges.add((first+"_"+str(i), second+"_"+str(j),weight))
    a = list(a)
    b = list(b)

    # temporary
    # a = [i for _ in range(1, 38)]
    # b = [i for _ in range(1, 55)]
    # first = '501'
    # second = '502'
    # edges = EG
    # ---------------

    for i in range(len(a)):
        a[i] = first+"_"+str(a[i])
    for i in range(len(b)):
        b[i] = second+"_"+str(b[i])
    for i in edges:
        print(i)
    T.get_tracking(a, b, edges)     
    return edges


#TRACKING GRAPH
def createTrackingTree():
    t1 = 33
    t2 = t1 + 1
    inputFile1 = inputpath+"nodes_t"+str(t1)+".pickle"
    pickle_in = open(inputFile1,"rb")
    nodes_in_timestep1 = pickle.load(pickle_in)
    pickle_in.close()
    inputFile = inputpath+"nodes_t"+str(t2)+".pickle"
    pickle_in = open(inputFile,"rb")
    nodes_in_timestep2 = pickle.load(pickle_in)
    pickle_in.close()


    volume_t1 = nodes_in_timestep1["volume"]
    volume_t2 = nodes_in_timestep2["volume"]
    a=set(volume_t1)
    b=set(volume_t2)
    a.remove(-1)
    b.remove(-1)
    edges = connectedComponents(volume_t1, volume_t2,a,b,str(t1),str(t2))
        #nodes_in_timestep1=nodes_in_timestep2
    # for i in edges:
    #     print(i)
        
    return edges