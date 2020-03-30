fin = open('C:\\Users\\Ani\\Downloads\\rosalind_subs_1_dataset.txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
text = fin.readlines()
dna,pattern = text[0].replace("\n",""), text[1].replace("\n","")

t = {i:dna[i] for i in range(0,len(dna)-len(pattern)+1) if dna[i:i+len(pattern)]==pattern}

fout.write(' '.join(map(str,list(t))))
    
fin.close()
fout.close()