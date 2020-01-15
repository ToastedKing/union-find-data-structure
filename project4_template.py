import math
#from sklearn import datasets

#digits = datasets.load_digits()
#digits_points = list(digits.data)
#digits_points = [list(point) for point in digits_points]

#iris = datasets.load_iris()
#iris_points = list(iris.data)
#iris_points = [list(point) for point in iris_points]

class Node:
   
    def __init__(self, key):
        self.value = key
        self.size = 0
        self.pointer = None
   

def make_union_find(n):
    #YOU DO
    nodeList = []
    node = 0
    while node != n: # makes nodes list objects 0 : n-1
        nodeList.append(Node(node))
        node = node+1
    return nodeList

def find(node):
    #YOU DO
    if node.pointer == None: # head pointer is itsled
        return node
    else:
        return find(node.pointer) # finds head pointer by following the pointers

       
def join(first, second):
    #YOU DO

    if first.size >= second.size: # first is bigger then second
        second.pointer = first  #attaches second to bigger
        first.size = first.size + second.size #recounts size
    else: #seoond is bigger
        first.pointer = second  #attaches first to bigger
        second.size = second.size + first.size #recounts size
    
def distance(x,y):
    counter = 0
    for i in range(len(x)): #can find distance of any size dimminsion
        dis = (pow(x[i] - y[i], 2)) # dis formula
        counter = counter + dis # summation
    return math.sqrt(counter) 
        
def make_graph(points):
    #YOU DO
    graph = []
    for i in range(len(points)): #graphs all poiunts
        for j  in range(i + 1, len(points)): 
            dis = distance(points[i], points[j])# takes distance of the points
            graph.append((dis,i,j)) # makes list of the graph
    return graph

def sortedEdges(edge):
    return edge[0] #graves the weight of a sorted graph

def cluster(points, k):
    #YOU DO
    
    graph = make_graph(points)

    sortedGraph = sorted(graph, key = sortedEdges) #make sorted edges

    unionFind = make_union_find(len(points)) # makes node objects
  
    length = len(points) #coounts the nodes / edges
    for i in range(0,len(sortedGraph)): #finds represntaive of the graph
        parent1 = find(unionFind[sortedGraph[i][1]])
        parent2 = find(unionFind[sortedGraph[i][2]])

        #if they are diffrent
        if (parent1.value != parent2.value):
            join(parent1, parent2) #sorts the two
            length = length - 1 #keeps count of the edges
        if length == k: #once cluster limit is reach then stop
            break
    
    return unionFind    

    
def cluster_distribution(components, classes, dataset):
    """Takes a union-find data structure (a list of nodes, linked together
    in connected components), a list of classes, and the dataset that the
    structure is built from, and returns a dictionary that determines how
    many times each class occurs within each of the connected components."""
    
    reps = set([find(node).val for node in components])
    counts = {}
    for r in reps:
        counts[r] = [0 for c in classes]
    for node in components:
        rep = find(node).val
        actual_class = dataset.target[node.val]
        counts[rep][actual_class] += 1
    return counts

#This small test should result in three clusters, each with 3 datapoints
small_test = [[1],[2],[3],[5],[6],[7],[9],[10],[11]]
components = cluster(small_test, 3)
for node in components:
    print(find(node).value)
#box = cluster(digits_points, 10)
#counts = cluster_distribution(box, [0,1,2,3,4,5,6,7,8,9], digits)
#print("flower")

#flower = cluster(iris_poiints, 3)
#counts = cluster_distribution(flower, [0,1,2], iris)
