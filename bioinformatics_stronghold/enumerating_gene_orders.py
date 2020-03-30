fin = open('C:\\Users\\Ani\\Downloads\\rosalind_perm.txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

f = fin.readline()
k = int(f)

import itertools

reads = list(map(" ".join, itertools.permutations(''.join(map(str,range(1,k+1))))))

fout.write(str(len(reads))+"\n")
for i in reads:
    fout.write(i+"\n")

fin.close()
fout.close()