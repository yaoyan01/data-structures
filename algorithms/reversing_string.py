class SimpleStack: 
    def __init__(self):
        self.stack = [] 
        self.size = 0
    
    def push(self, value):
        self.stack.append(value)
        self.size += 1 
    
    def pop(self):
        if self.size > 0:
            self.size -= 1 
            return self.stack.pop()
        return None 
    
    def peek(self):
        if self.size > 0:
            return self.stack[-1]
        return None 

    def print(self):
        if self.size == 0:
            print("Stack is empty")
        else:
            print("Stack contents (top to bottom):")
            print(self.stack)

def reverse_string(s):
    stack = SimpleStack()
    output = ''

    for c in s:
        stack.push(c)

    while stack.size > 0:
        output += stack.pop()
    
    return output 

def reverse_string2(s):
    return s[::-1] 
