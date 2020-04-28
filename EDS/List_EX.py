from EDS import List


#Esercizio 10.2-2
#Attenzione: L'esempio utilizza una lista doppiamente concatenata,in realtà però la concatenazione all'indietro non viene utilizzata,
#basta quindi ignorare le parti di assegnazione dell'attributo "prev" dell'elemento
class Stack: #Stack con lista
    def __init__(self): #Non abbiamo bisogno di maxsize
        self.stack = List.List()
        self.top = self.stack.Head

    def StackEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def Push(self,e):
           self.stack.Insert(List.ListObj(e))


    def Pop(self):
        x = self.stack.Head
        self.stack.Delete(x)  #O(1)
        return x

#Esercizio 10.2-3
class Queue: #Queue con lista
    def __init__(self): #Non abbiamo bisogno di maxsize
        self.queue = List.List()
        self.head = self.queue.Head
        self.tail = self.queue.Head

    def Enqueue(self,e): #Senza sfruttare altri attributi non mi viene in mente come andare sotto O(n)..altrimenti sull'insert appoggerei la x su var locale
        x = List.ListObj(e)
        if self.queue.Head != None:
            y = self.queue.Head
            while y.next != None:
                y = y.next
            y.next = x
        else:
            self.queue.Head = x

    def Dequeue(self):
        x = self.queue.Head
        if x != None:
            self.queue.Head = self.queue.Head.next
            return x
        else:
            raise Exception("Underflow")

    def Print(self):
        print(self.queue.Print())


