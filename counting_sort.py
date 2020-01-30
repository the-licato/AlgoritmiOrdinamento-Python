def counting_sort(A,k):
    B=[0 for i in range(len(A))] #creo un vettore di dimensione len(A) e lo riempio di '0'
    C=[0 for i in range(k+1)] #creo un vettore di dimensione k+1 e lo riempio di '0'
    
    for element in A:
        C[element]+=1
        #C[i] e' il numero di occorrenze di i
    
    for i in range(1,k+1):
        C[i]+=C[i-1]
        #C[i] e' il numero di elementi <= i

    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1

    return B
