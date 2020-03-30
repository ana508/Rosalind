fin = open('C:\\Users\\Ani\\Downloads\\rosalind_splc_2_dataset.txt')
fout=open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
lst = ''.join(fin.read().split('\n')).split('>')
lst.remove('')
dna,introns = lst[0],lst[1:]
table = {
    "UUU":"F","UUC":"F","UUA":"L","UUG":"L",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "UAU":"Y","UAC":"Y","UAA":"*","UAG":"*",
    "UGU":"C","UGC":"C","UGA":"*","UGG":"W",
    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
    "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}

for i in introns:
    dna = dna.replace(i[13:],"")
dna = dna[13:]
rna = dna.replace("T","U")

def translate(seq):
    protein = ""
    for i in range(0,len(seq),3):
        codon = seq[i : i + 3]
        protein += table[codon]
    return protein

fout.write(translate(rna)[:-1])

fin.close()
fout.close()