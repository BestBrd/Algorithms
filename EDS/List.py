class ListObj:
    def __init__(self,key,next = None,prev = None):
        self.key = key
        self.next = next
        self.prev = prev


class List:
    def __init__(self,Head = None):
        self.Head = Head

    def Search(self,k):
        x = self.Head
        while x != None and x.key != k:
            x = x.next
        return x

    def Insert(self,x):
        x.next = self.Head
        if x.next != None:
            x.prev = x
        self.Head = x
        x.prev = None

    def Delete(self,x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.Head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def Print(self):
        x = self.Head
        while x.next != None:
            print(x.key)
            x = x.next





class ListWithSentry(List):
    def __init__(self):
        self.Nil = ListObj(None)
        self.Head = self.Nil

    def Search(self,k): #Uguale alla Lista normale
        x = self.Nil.next
        while x != self.Nil and x.key != k:
            x = x.next
        return x

    def Insert(self,x):
        x.next = self.Nil.next
        if self.Nil.next != None: #Richiesto anche se non specificato nello pseudocodice
            self.Nil.next.prev = x
        self.Nil.next = x
        x.prev = self.Nil

    def Delete(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def Print(self):
        x = self.Nil
        while x != self.Nil:
            print(x.key)
            x = x.next


