class Counter:
    def __init__(self,max):
        self.max = max
        self.current = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
        
c = Counter(5)

for num in c:
    print(num)