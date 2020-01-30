# MERGE SORT ALGORITHM
# Descrizione: https://www.thelicato.it/blog/algoritmi-di-ordinamento-merge-sort-in-python/

#Si e' realizzata una funzione di MergeSort che ordina tutto il vettore,
#dunque l'unico parametro in ingresso e' il vettore stesso
import sys

def merge(array,lefthalf,righthalf):
    lefthalf.append(sys.maxsize)
    righthalf.append(sys.maxsize)
    j=0
    i=0
    for k in range(len(array)):
        if lefthalf[i]<=righthalf[j]:
            array[k]=lefthalf[i]
            i=i+1
        else:
            array[k]=righthalf[j]
            j=j+1

def merge_sort(array):
    if len(array)>1:
        mid = len(array)//2  #divisione intera per difetto
        lefthalf = array[:mid] #prendo la prima meta' del vettore
        righthalf = array[mid:] #prendo la seconda meta' del vettore
        merge_sort(lefthalf)
        merge_sort(righthalf)     
        merge(array,lefthalf,righthalf)
