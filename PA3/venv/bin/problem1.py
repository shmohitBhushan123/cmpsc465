#GLOBAL VARIABLES
clock = 0
visited = []
num_cc = 0
postlist = []
visitedCC = []

#CREATE GRAPH USING HASH TABLE

#get first line values vertices and indexes
rawArray = input().split(" ")
vertices = int(rawArray[0])
edges = int(rawArray[1])

for i in range(vertices):
    visited.append(0)
for i in range(vertices):
    visitedCC.append(0)

#create dictionary for hash table
vertdict = {}

#create primary keys for dictionary
for i in range(1, vertices+1):
    vertdict[i] = []


#fill vertices with adjacent vertices
for i in range(0, edges):
    rawInput = input().split(" ")
    key = int(rawInput[0])
    pair = int(rawInput[1])
    vertdict[key].append(pair)


#CREATE REVERSE GRAPH TO FIND MAGIC NUMBER

#create a reverse graph
vertdictRvrs = {}

#create primary keys for dictionary
for i in range(1, vertices+1):
    vertdictRvrs[i] = []

for i in range(1, vertices+1):
    for j in range(len(vertdict[i])):
        vertdictRvrs[vertdict[i][j]].append(i)




#CREATE FUNCTIONS DFS AND EXPLORE TO GET REVERSE LINEARIZATION

def DFS(verdictRvrs):
    global clock

    clock =1
    for i in range(0, vertices):
        if (visited[i] ==0):
            explore(verdictRvrs,i)

def explore(verdictRvrs, vi):
    global clock

    visited[vi] = 1

    #pre[vi] = clock
    clock+=1

    for e in range(0, len(vertdictRvrs[vi+1])):
        if (len(vertdictRvrs[vi+1]) == 0):
            continue
        elif(visited[(vertdictRvrs[vi+1][e])-1]==0):
            explore(vertdictRvrs, ((vertdictRvrs[vi+1][e])-1))
    #post[vi] = clock
    clock += 1
    postlist.append(vi+1)

linearization = []
DFS(vertdictRvrs)
#reverse postlist and convert to linearization
for i in range(0, len(postlist)):
    linearization.append(postlist[i])
linearization.reverse()



#CREATE DFS AND EXPLORE AGAIN TO GET NUM_CC


def DFSCC(verdirect):
    global num_cc
    for i in linearization:
        v = i-1
        if (visitedCC[v] ==0):
            num_cc +=1
            exploreCC(verdirect,v)


def exploreCC(graph, vi):
    global num_cc
    visitedCC[vi] = num_cc
    for e in range(0, len(graph[vi + 1])):
        if (len(graph[vi + 1]) == 0):
            continue
        elif (visitedCC[(graph[vi + 1][e]) - 1] == 0):
            exploreCC(graph, ((graph[vi + 1][e]) - 1))


DFSCC(vertdict)
print(num_cc)