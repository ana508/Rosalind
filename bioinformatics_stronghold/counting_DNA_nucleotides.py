fin = open('C:\\Users\\Ani\\Downloads\\rosalind_dna_1_dataset.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
dna = fin.readline().replace("\n","")
def count(text):
    return text.count("A"), text.count("C"), text.count("G"), text.count("T")
for i in count(dna):
    fout.write(str(i) + " ")

fin.close()
fout.close()