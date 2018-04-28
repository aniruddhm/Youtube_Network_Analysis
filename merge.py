f = open('0301/allmodified.txt', 'a')
f1 = open('0301/0modified.txt','r')
f2 = open('0301/1modified.txt','r')
f3 = open('0301/2modified.txt','r')
f4 = open('0301/3modified.txt','r')

for line in f1:
    f.write(line)
for line in f2:
    f.write(line)
for line in f3:
    f.write(line)
for line in f4:
    f.write(line)

f.close()
f1.close()
f2.close()
f3.close()
f4.close()