import igraph
import os
import matplotlib.pyplot as plt
import math


class analysis:
    def calAvgDegree(self,type,inputfile):
        f = open(inputfile, 'r')
        g = igraph.Graph.Read_Ncol(f, directed=True)
        outdegree = g.degree(type=type)
        # print(len(g.vs))
        dict = {}
        for degree in outdegree:
            if degree in dict:
                dict[degree] = dict[degree]+1
            else:
                dict[degree] = 1
        # print dict
        f.close()

        degreearray=[]
        nodewiththatdegreearray = []
        for degree in sorted(dict.keys()):
            degreearray.append(degree)
            nodewiththatdegreearray.append(dict[degree])
        print(degreearray)
        print(nodewiththatdegreearray)

        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        plt.plot(degreearray,nodewiththatdegreearray, 'ro')
        # for xy in zip(degreearray, nodewiththatdegreearray):
        #     ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
        plt.grid()
        plt.show()

        count = 0
        for i in nodewiththatdegreearray:
            count = count+i
        print(count)
        for i,x in enumerate(nodewiththatdegreearray):
            nodewiththatdegreearray[i] = (float(x)/count) * 100
        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        plt.plot(degreearray,nodewiththatdegreearray, 'ro')
        # for xy in zip(degreearray, nodewiththatdegreearray):
        #     ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
        plt.grid()
        plt.show()

    def main(self):
        # self.calAvgDegree("in", "0301/0modified.txt")
        f = open('0301/allmodified.txt','r')
        g = igraph.Graph.Read_Ncol(f,directed=False)
        # print(g.clusters(mode="WEAK"))
        # print(g.transitivity_avglocal_undirected(mode="nan"))
        print(g.average_path_length())
        # hubscore = igraph.Graph.hub_score(g,scale=True)
        # nodes = [i for i in xrange(1,len(g.vs)+1)]
        # plt.plot(nodes,hubscore,'ro')
        # plt.grid()
        # plt.show()

if __name__ == '__main__':
    analysis = analysis()
    analysis.main()
