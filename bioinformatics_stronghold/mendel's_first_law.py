fin = open('C:\\Users\\Ani\\Downloads\\rosalind_iprb.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
k,m,n = map(int, fin.readline().split())

def com(n):
    return float(n*(n-1)/2)

fout.write(str(1-(com(n)+com(m)/4+m*n/2)/com(k+m+n)))

fin.close()
fout.close()