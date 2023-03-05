## Valerija Drozda 221RDB450

import sys
import threading
import numpy

def compute_height(n, parents):
    
    empty = numpy.zeros(n)

    for i in range(n):
        if parents[i] != -1:
            index = parents[i]
            empty[index] = 1
    
    answer = int(np.numpy(empty) + 1)
    print(answer)



def main():
    
    text = input()

    if "I" in text:
        
        n = int(input())
        
        string = input()
        parents = numpy.asarray(list(map(int, string.split())))

        if n == parents.size:
            compute_height(n, parents)       
    
    elif "F" in text:
        file_n = input().strip()
        if "a" in file_n:
            return
        else:
            with open('test/' + file_n, 'r') as f:
                
                n = int(f.readline())
                
                string = f.readline()
                parents = numpy.asarray(list(map(int, string.split())))

                if n == parents.size:
                    compute_height(n, parents)
    
   
threading.Thread(target=main).start()