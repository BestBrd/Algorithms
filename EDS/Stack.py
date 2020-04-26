#Insert = Push
#Delete = Pop

class Stack:
    def __init__(self,maxsize):
        self.stack = [None] * maxsize
        self.maxsize = maxsize
        self.top = -1

    def StackEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def Push(self,e):
        if  self.top < self.maxsize-1:
            self.top += 1
            self.stack[self.top] = e
        else:
            raise Exception("Overflow")

    def Pop(self):
        if not self.StackEmpty():
            self.top -= 1
            return self.stack[self.top+1]
        else:
            raise Exception("Underflow")


stack = Stack(2)
stack.Push(108)
stack.Push(123)
stack.Push(123)
print(stack.Pop())
print(stack.Pop())
