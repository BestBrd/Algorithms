import sys

def BubbleSort(array):
    for i in range(0,len(array)-1,1):
        for j in range(0,len(array)-1,1):
            if array[j]>array[j+1]:
                c = array[j]
                array[j] = array[j+1]
                array[j+1] = c

def InsertionSort(array):
    for j in range(1,len(array),1):
        key = array[j]
        i=j-1
        while i>0 and array[i]>key:
            array[i+1] = array[i]
            i-=1
        array[i+1] = key

def Merge(array,p,q,r): #p è l'inizio,q la meta,r la fine
    n1 = q-p+1 #lunghezza primo sottoarray
    n2 = r-q   #lunghezza secondo sottoarray

    #Eseguo i seguenti passi:
    #-Inizializzo i 2 sottoarray L e R
    #-L contiene la prima meta e R la seconda meta dell'array
    #-Aggiungo 2 sentinelle in fondo per il confronto
    L = array[:q] + [sys.maxsize]
    R = array[q:] + [sys.maxsize]

    #imposto i contatori
    i = 0
    j = 0

    for k in range(0,len(array)):
        if(L[i]<R[j]):
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1

def MergeSort(array,p,r): #p è l'inizio,r la fine
    if p<r:
        q = (p+r)//2
        MergeSort(array,p,q)
        MergeSort(array,q+1,r)
        Merge(array,p,q,r)


def Partition(arrray, p, r):
    i = p - 1  # index of smaller element
    pivot = arrray[r]  # pivot
    for j in range(p, r):
        if arrray[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arrray[i], arrray[j] = arrray[j], arrray[i]

    arrray[i + 1], arrray[r] = arrray[r], arrray[i + 1]
    return i + 1


def QuickSort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

def QuickSort(array,p,r):
    if p<r:
        q= Partition(array,p,r)
        QuickSort(array,p,q-1)
        QuickSort(array,q+1,r)

