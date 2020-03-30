fin = open('C:\\Users\\Ani\\Downloads\\rosalind_fib_1_dataset.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
n,k = map(int, fin.readline().split())

def wabbits(n, k):
   if n == 0:
    return 0
   if n == 1:
    return 1
   else:
    return wabbits(n-1, k) + k*wabbits(n-2, k)

fout.write(wabbits(n,k))

fin.close()
fout.close()