class SimpleStack: 
    def __init__(self):
        self.stack = [] 
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None 
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None 

