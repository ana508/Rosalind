import re
fin = open('C:\\Users\\Ani\\Downloads\\rosalind_orf (2).txt','r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
rem = ''.join(fin.read().split('\n')).split('>')
rem.remove('')
dna = rem[0][13:]

def dna_codon_map():
    codon_map = {}
    with open('C:\\Users\\Ani\\Downloads\\RNA_codon_table.txt') as f:
        for line in f:
            pair = line.strip().split()
            pair[0] = pair[0].replace('U', 'T')
            if len(pair) == 2:
                codon_map[pair[0]] = pair[1]
            else:
                codon_map[pair[0]] = '*'
    return codon_map

orf_regex = re.compile(r"(?=(M\w*\*))")
orfs = set()

def reverse_complement(text):
    return "".join(([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[i]
                   for i in list(text)])[::-1])
def orf_finder(dna):
    for orf in range(3):
        translated = ''.join([dna_codon_map()[dna[i:i+3]]
                              for i in range(orf, (int((len(dna)-orf)/3)*3), 3)])
        for i in orf_regex.finditer(translated):
            orfs.add(i.group(1)[:-1])
    for orf in range(3):
        translated = ''.join([dna_codon_map()[reverse_complement(dna)[i:i+3]]
                              for i in range(orf, (int((len(dna)-orf)/3)*3), 3)])
        for i in orf_regex.finditer(translated):
            orfs.add(i.group(1)[:-1])
    return orfs

for i in orf_finder(dna):
    fout.write(i + "\n")
    
fin.close()
fout.close()
