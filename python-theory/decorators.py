#wszystko w pyyhonie, nawet klasy, to obiekty

#można przekazywać funkcje jako argumenty

def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func, x):
    result = func(x)
    return result

#funkcja moze tez zwrocic innafunkcje:

def is_called():
    def is_returned():
        print('hello')
    return is_returned

new = is_called()

new()

# nazywa się je callable -> bo mogą być called
# kazdy obiekt, ktory implementuje __call__() sie tak nazywa
# wiec decorator to callable, ktory zwraca callable

def make_pretty(func):
    def inner():
        print('i got decorated')
        func()
    return inner

def ordinary():
    print('I am oridinary')

oridinary()

pretty = make_pretty(ordinary)
pretty()

#to jest to samo co ordinary = make_pretty(ordinary)

@make_pretty
def ordinary():
    print('i am ordinary')

#dekorator z parametrami



def smart_divide(func):
    def inner(a, b):
        print('I am going to divide ', a, ' and ', b)
        if b ==0:
            print('nie da sie')
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

#magia jest przy args i kwargs

def work_for_all(func):
    def inner(*args, **kwargs):
        print('i can decorate any function')
        return func(*args, **kwargs)
    return inner

#chaining
def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*'*30)
    return inner

def dupa(func):
    def inner(*args, **kwargs):
        print('dupa')
        func(*args,**kwargs)
        print('kał')
    return inner

@star
@dupa
def printer(msg):
    print(msg)

printer('sram')