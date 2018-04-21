import sys
import os

class Preprocessing:

    def dataprocessing(self, file):
        edgelist = {}
        vertices = []
        f = open(file, 'r')
        for line in f :
            line = line.replace('\r','')
            line = line.replace('\n','')
            array = line.split('\t')
            edgelist[array[0]] = array[9:]
            vertices.append(array[0])
            vertices = vertices + array[9:]
        uniquevertices = len(set(vertices))
        f1 = open('0301/0modified.txt', 'w')
        for key in edgelist.keys():
            for value in edgelist[key]:
                f1.write(key + ' ' + value + '\n')
        f1.close()
        return uniquevertices

    def main(self):
        uniquevertices = self.dataprocessing('0301/0.txt')
        print(uniquevertices)
        os.system("python /home/saktlonda/Documents/youtuberelatedvideoanalysisandprediction/ab.py")

if __name__ == '__main__':
    p = Preprocessing()
    p.main()

