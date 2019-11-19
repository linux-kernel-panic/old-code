class Stack:
    def __init__(self,data=[]):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return self.data

    def __add__(self,other):
        unique = self.data.copy()
        for item in other.data:
            if item not in unique:
                unique.append(item)
            else:
                continue
        return Stack(unique)
    
    def remove(self):
        if len(self.data) > 1:
            self.data = self.data[:-1]
        else:
            print("You cannot remove any more data")

    def ret(self):
        return self.data

    def add(self,value):
        self.data.append(value)
    
    def get_data(self):
        return self.data[-1]



##class Queue(Stack):
##    def get_data(self):
##        return self.data[0]
##    
##    def remove(self):
##        if len(self.data) > 1:
##            self.data = self.data[1:]
##        else:
##            print("You cannot remove any more data")

class Queue:
    def __init__(self,data=[]):
        self.stack_right = Stack(data)
        self.stack_left = Stack()

    def add(self,item):
        stack_right.add(item)

    def remove(self):
        if self.left_stack.ret():
            self.left_stack.remove()
        else:
            right_data = stack_right.ret()
            self.stack_left = Stack(right_data.reverse())
            for i in range(len(right_data)):
                stack_right.remove()
                

class HashMap:
    def __init__(self):
        self.data = []
        self.num = 0
        self.keys = []
        
    def __eq__(self,other):
        return self.data == other.data
    
    def add_key_value(self,key,value):
        self.data.append([key, value, self.num])
        self.keys.append(key)
        self.num += 1
        
    def get_value_from_key(self,key):
        for ls in self.data:
            if ls[0] == key:
                return ls[1]
            
    def get_value_from_index(self,index):
        for ls in self.data:
            if ls[2] == index:
                return ls[1]

hashmsp = HashMap()
stack = Stack(["bob", "bill", "jill"])
queue = Queue(["ipad","bear","light"])
