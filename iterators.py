class Iterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1
    
# for i in Iterator(1, 5):
#     print(i)
