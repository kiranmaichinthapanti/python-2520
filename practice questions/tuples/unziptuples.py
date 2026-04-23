t = ((1,'a'), (2,'b'), (3,'c'))

# a,b = zip(*t)
# print(a)
# print(b)

print(tuple(zip(*t)))