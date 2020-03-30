fin = open('C:\\Users\\Ani\\Downloads\\rosalind_revp.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
text = fin.readlines()
dna = ''
for i in text[1:]:
    dna += i.replace("\n","")
def  reverse_palindrome(text):
    dc = {}
    for i in range(4,13):
        for j in range(len(text)-i+1):
            pattern = text[j:j+i]
            reverse_pattern = "".join(([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[l]
                    for l in list(pattern)])[::-1])
            if pattern == reverse_pattern:
                dc[str(j+1)] = len(pattern)
    return dc

result = reverse_palindrome(dna)

for k,v in result.items():
    fout.write(k+" " + str(v)+"\n")