fin = open('C:\\Users\\Ani\\Downloads\\rosalind_rna_1_dataset.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
dna = fin.readline().replace("\n","")

def transcribe(text):
    text = text.replace("T","U")
    return text

fout.write(transcribe(dna))

fin.close()
fout.close()