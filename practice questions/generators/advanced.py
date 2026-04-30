#  Create an infinite generator
def infiniteNumbers():
    i = 1
    while True:
        yield i
        i += 1

gen = infiniteNumbers()

for _ in range(5):
    print(next(gen))

# Build a generator pipeline (filter + transform)
pipeline = (i*i for i in range(1,11) if i%2 == 0)
for value in pipeline:
    print(value)