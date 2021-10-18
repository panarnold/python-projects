# Iterator - obiekt, który umozliwia poruszanie się przez container
# iterator umozliwia podroz i dostep do daty, ale nie wykonuje on uteracji, dlatego są: Iterable, Iterator, Iteration

# ITERABLE
# każdy obiekty pytona który ma __iter__ lub __getitem__ metode, która zwraca iterator albo może brać indeksy. Innymi słowy, to każdy obiekt, który zapewnia nam ITERATOR

# ITERATOR
# kazdy obiekt, ktory ma __next__

# ITERATION
# proces pozyskiwania itemu z np listy

# GENERATORS
# generatory, to iteratory, które przechodzą tylko raz - nie przechowują w pamięci, generują wartości on a fly
# częśto implementowane jako funkcje, ale nie zwracają wartości, tylko robią YIELD.yield

def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print('***')
fibon(4)

print('***')
# stringi są iterable, ale zeby zrobic z nich iterator, trzeba dac je do iter(str), wtedy zadziala next np

name = 'kutasina'
piter = iter(name)

print(next(piter))
print(next(piter))
