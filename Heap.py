import sys

class MaxHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.Front = 1

    def parent(self,i):
        return i//2

    def leftChild(self,i):
        return i*2

    def rightChild(self,i):
        return (i*2) +1

    def isLeaf(self,i):
        if i<=self.size and i>= self.size//2:
            return True
        return False

    def Swap(self,p,f):
        if p<=self.size and f<=self.size:
            self.Heap[p],self.Heap[f] = self.Heap[f],self.Heap[p]

    def MaxHeapify(self,i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        maximum = i

        if left<self.size and self.Heap[i] < self.Heap[left]:
            maximum = left
        if right<self.size and self.Heap[i] < self.Heap[right]:
            maximum = right

        if maximum!=i:
            self.Swap(i,maximum)
            self.MaxHeapify(maximum)

    def Insert(self,i):
        if self.maxsize >= self.size:
            return
        self.size+=1
        self.Heap[self.size] = i

        current = self.size

        while(self.Heap[current] > self.Heap[self.parent(current)]):
            self.Swap(current,self.parent(current))
            current = self.parent(current)

    def Print(self): #Non funziona
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def PrintHeap(self):
        print(self.Heap)

    def ExtractMax(self):
        max = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -=1
        self.MaxHeapify(self.Front)
        return max

    @classmethod
    def BuildMaxHeap(cls,arr = []):
        maxheap = MaxHeap(len(arr))
        maxheap.Heap = arr
        maxheap.size = len(arr)

        for i in range(len(arr)//2,-1,-1):
            maxheap.MaxHeapify(i)
        return maxheap



maxheap = MaxHeap.BuildMaxHeap([10,5,2,30,14,1,34,16])
maxheap.PrintHeap()