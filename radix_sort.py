import sys
from utils import *

def counting_sort_radix(A,cifra):
    array=A[:] #creo una copia del vettore da ordinare

    C=[0 for i in range(10)]

    for element in array:
        C[element//10**(cifra-1)%10]+=1

    for i in range(1,10):
        C[i]=C[i]+C[i-1]
    
    for j in range(len(array)-1,-1,-1):
        A[C[array[j]//10**(cifra-1)%10]-1]=array[j]
        C[array[j]//10**(cifra-1)%10]-=1

def radix_sort(array,num_cifre):
    for cifra in range(1,num_cifre+1):
        counting_sort_radix(array,cifra)