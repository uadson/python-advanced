from iterators import Iterator

def generator():
    for i in Iterator(1, 6):
        yield i
        
gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
