fin = open('C:\\Users\\Ani\\Downloads\\rosalind_hamm_1_dataset.txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
text = fin.readlines()
s1,s2 = text[0].replace("\n",""), text[1].replace("\n","")

def hamming_distance(s1,s2):
    return sum(c1!=c2 for c1,c2 in zip(s1,s2))
fout.write(str(hamming_distance(s1,s2)))

fin.close()
fout.close()