from queue import PriorityQueue
import sys

# Global variables
dist = []
n = 0
#CREATE GRAPH CLASS


#get first line values vertices and indexes
rawArray = input().split(" ")
vertices = int(rawArray[0])
edges = int(rawArray[1])
source = int(rawArray[2])


#create dictionary for hash table
vertdict = {}

# list for
S = []


#create primary keys for dictionary
for i in range(1, vertices+1):
    vertdict[i] = {}


#fill vertices with adjacent vertices
for i in range(0, edges):
    rawInput = input().split(" ")
    key = int(rawInput[0])
    pair = int(rawInput[1])
    length = int(rawInput[2])
    #vertdict[key]= pair
    vertdict[key][pair] = {}
    vertdict[key][pair] = length


print(vertdict)
'''
beans = heapq
def dij(graph, edgelen, source):
    for i in range (0, vertices-1):
        dist[i].append(sys.maxsize)
    for i in range(1, vertices + 1):
        beans.heappush()
    dist[s-1] = 0
    decrease_key(beans, source, 0)
    while empty(beans)==false :
        u = find_Min(beans)
        delete_min(beans)
        ##
        # Ok this is bad
        # In the next line, e is the index but the way the values are taken, like graph[1][2]... 2 is the value not the index...
        ##
       # for e in range(0, len(graph[s])):
            if dist[v] > graph[s][e])
'''
def empty(beans):
    if n==0:
        return true
    else:
        return false

def insert(beans, x):
    global n
    n = n+1
    S[n]=x
    bubble_up(S, n)

def find_min(beans):
    return S[1]

def delete_min(beans):
    global n
    S[1] = S[n]
    n = n-1
    sift_down(S, 1)

def decrease_key(beans, k, new_key):
    S[k].key = new_key
    bubble_up(S,k)

def bubble_up(S, k):
    p = k/2
    if S[k].key < S[p].key:
        temp = S[k]
        S[k] = S[p]
        S[p] = S[k]
        bubble_up(S, p)

def sift_down(S, k):
    c = min
    if S[k].key > S[c].key:
        temp = S[k]
        S[k] = S[c]
        S[c] = S[k]
        sift_down(S, c)