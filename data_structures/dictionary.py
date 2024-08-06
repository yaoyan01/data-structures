class SimpleDict: 
    def __init__(self):
        self.size = 100 
        self.bucket = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        hashing_constant = 10 
        return hash(key) % hashing_constant 
    
    def insert(self, key, value):
        index = self._hash(key)
        for arr in self.bucket[index]:
            if arr[0] == key:
                arr[1] = value 
                return 
        self.bucket[index].append([key, value])
    
    def delete(self, key):
        return  
    
    def contains(self, key): 
        return 
    
    