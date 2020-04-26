#Insert = Enqueue
#Delete = Dequeue

class Queue:

    def __init__(self,maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0

    def Enqueue(self,e): #Versione senza controlli (libro)
        self.queue[self.tail] = e
        if self.tail == self.maxsize-1:
            self.tail = 0
        else:
            self.tail += 1

    def Dequeue(self):  #Versione senza controlli (libro)
        x = self.queue[self.head]
        if self.head==self.maxsize-1:
            self.head == 0
        else:
            self.head += 1
        return x

 ##Da aggiungere versione con controlli (10.1-4)
