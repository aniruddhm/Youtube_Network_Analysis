import sys
import os
import random

class Preprocessing:

    def dataprocessing(self, inputfile, outputfile):
        edgelist = {}
        vertices = []
        f = open(inputfile, 'r')
        for line in f :
            line = line.replace('\r','')
            line = line.replace('\n','')
            array = line.split('\t')
            edgelist[array[0]] = array[9:]
            vertices.append(array[0])
            vertices = vertices + array[9:]
        uniquevertices = len(set(vertices))
        f.close()
        f1 = open(outputfile, 'w')
        for key in edgelist.keys():
            for value in edgelist[key]:
                f1.write(key + ' ' + value + '\n')
        f1.close()
        return uniquevertices

    def randmoizefiledata(self,inputfile,outputfile):
        f = open(inputfile,'r')
        f1 = open(outputfile,'w')
        entire_file = f.read()
        file_in_a_list = entire_file.split("\n")
        num_lines = len(file_in_a_list)
        random_nums = random.sample(xrange(num_lines), 500)
        for i in random_nums:
            f1.write(file_in_a_list[i] + "\n")
        f1.close()
        f.close()

    def main(self):
        uniquevertices = self.dataprocessing('0301/0.txt','0301/0modified.txt')
        print(uniquevertices)
        uniquevertices = self.dataprocessing('0301/1.txt','0301/1modified.txt')
        print(uniquevertices)
        uniquevertices = self.dataprocessing('0301/2.txt','0301/2modified.txt')
        print(uniquevertices)
        uniquevertices = self.dataprocessing('0301/3.txt','0301/3modified.txt')
        print(uniquevertices)
        # self.randmoizefiledata('0301/0modified.txt', '0301/0randommodified.txt')


if __name__ == '__main__':
    p = Preprocessing()
    p.main()

