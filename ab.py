import igraph
import os

# print "hi"
f = open("0301/.0modified.txt", 'r')
g = igraph.Graph.Read_Ncol(f, directed=True)
f.close()
g.vs['label'] = [i for i in range(1,5659)]
igraph.plot(g)
