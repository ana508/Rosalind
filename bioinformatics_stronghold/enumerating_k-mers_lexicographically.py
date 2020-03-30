fin = open('C:\\Users\\Ani\\Downloads\\rosalind_lexf.txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

f = fin.readlines()
text, k = f[0].replace("\n","").replace(" ",""), int(f[1].replace("\n",""))

import itertools

reads= ["".join(i) for i in itertools.product(text, repeat=k)]

for i in reads:
    fout.write(i+"\n")

fin.close()
fout.close()