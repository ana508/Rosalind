fin = open('C:\\Users\\Ani\\Downloads\\rosalind_fibd_1_dataset.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
n,m = map(int, fin.readline().split())                                                                     
rabbits = [1, 1]                                                               
months = 2                                                                     
while months < n:                                                              
    if months < m:                                                             
        rabbits.append(rabbits[-2] + rabbits[-1])                              
    elif months == m:                                        
        rabbits.append(rabbits[-2] + rabbits[-1] - 1)                          
    else:                                                                      
        rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[-(                  
            m + 1)])                                                           
    months += 1                                                                
fout.write(rabbits[-1]) 

fin.close()
fout.close()