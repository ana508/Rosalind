fin = open('C:\\Users\\Ani\\Downloads\\rosalind_revc_1_dataset.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
dna = fin.readline().replace("\n","")
def reverse_complement(text):
    return "".join(([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[i]
                   for i in list(text)])[::-1])

fout.write(reverse_complement(dna))

fin.close()
fout.close()