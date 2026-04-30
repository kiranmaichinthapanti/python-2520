# Create iterator for Fibonacci series
class Fibonacci:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return value
        else:
            raise StopIteration
        
fib = Fibonacci(4)
for num in fib:
    print(num)

# Build iterator that skips numbers (like step=2)
class StepIterator:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration
        
it = StepIterator(1,10,2)

for num in it:
    print(num)