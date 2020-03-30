fin = open('C:\\Users\\Ani\\Downloads\\rosalind_gc_2_dataset.txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

dna_strings = ''.join(fin.read().split('\n')).split('>')
dna_strings.remove('')

d = {}
for i in dna_strings:
    d[i[:13]] = ((i[13:].count('C') + i[13:].count('G')) / (len(i[13:])))*100
fout.write(max(d, key=d.get)+ "\n" + str(max(d.values())))

fin.close()
fout.close()