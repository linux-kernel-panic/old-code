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
h = HashMap()
