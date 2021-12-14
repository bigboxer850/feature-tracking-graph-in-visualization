xd = 192
yd = 64
zd = 48

def createNode(level,id):
    newNode = {}
    newNode['id'] = id
    newNode['level'] = level
    

    return newNode

def bfs(compNo,i,j,k,id):
    
    q=[]
    q.append((i, j, k))  
    while len(q):
 
        # dequeue front node and process it
        i, j, k = q[0]
        del q[0]
        compNo[((k * yd + j) * xd + i)] = id

        #if valid and unexplored neighbours then add them to queue
        if i+1<xd and compNo[((k * yd + j) * xd + i+1)]==-2:
            compNo[((k * yd + j) * xd + i+1)]=id
            q.append((i+1,j,k))
            #compNo=bfs(compNo,i+1,j,k,id)
        if j+1<yd and compNo[((k * yd + j+1) * xd + i)]==-2:
            compNo[((k * yd + j+1) * xd + i)]=id
            q.append((i,j+1,k))
            #compNo=bfs(compNo,i,j+1,k,id)
        if k+1<zd and compNo[(((k+1) * yd + j) * xd + i)]==-2:
            compNo[(((k+1) * yd + j) * xd + i)]=id
            q.append((i,j,k+1))
            #compNo=bfs(compNo,i,j,k+1,id)
        if i-1>=0 and compNo[((k * yd + j) * xd + i-1)]==-2:
            compNo[((k * yd + j) * xd + i-1)]=id
            q.append((i-1,j,k))
            #compNo=bfs(compNo,i-1,j,k,id)
        if j-1>=0 and compNo[((k * yd + j-1) * xd + i)]==-2:
            compNo[((k * yd + j-1) * xd + i)]=id
            q.append((i,j-1,k))
            #compNo=bfs(compNo,i,j-1,k,id)
        if k-1>=0 and compNo[(((k-1) * yd + j) * xd + i)]==-2:
            compNo[(((k-1) * yd + j) * xd + i)]=id
            q.append((i,j,k-1))
            #compNo=bfs(compNo,i,j,k-1,id)

    # newNode['componentMatrix']  = compNo  
    return compNo

def floodfill(i, j, k, level,id,compNo):
    # create a queue and enqueue starting pixel
    newNode = createNode(level,id)
    compNo=bfs(compNo,i,j,k,id)
    return (newNode,compNo)