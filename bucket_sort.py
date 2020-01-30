# BUCKET SORT ALGORITHM
# Descrizione: https://www.thelicato.it/blog/bucket-sort-in-python/

from utils import *
from insertion_sort import *

def bucket_sort(array):
    n=len(array)
    
    B=[[]for i in range(n)]
    for i in range(n):
        #insert A[i] into list B[[nA[i]]
        index=int(n*array[i])
        B[index].append(array[i])
    
    for i in range(n):
        #sort list B[i] with insertion sort
        insertion_sort(B[i])

    #Concatenate the lists B[0],....,B[n-1] in order
    C=[]
    for i in range(n):
        C=C+B[i]
    return C

