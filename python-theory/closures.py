# to jest jak przypisanie wartości z wykonanej funkcji do innej zmiennej?

def print_msg(msg):

    def printer():
        print(msg)

    return printer

another = print_msg('hello')
another()

# nawet gdy damy del print_msg to wartosc przy wywołaniu another zostanie

# warunki:
# funkcja zewn musi zwrocic funkcje wewn
# musi być funkcja nested

#po co? 
# avoid global values
# provide data hiding
# provide OOP solutions
# dobre, ale gdy więcej atrybutów do metody, wtedy lepiej porobić klasy

#przykład:

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# multipler of 3

times3 = make_multiplier_of(3)

# of5

times5 = make_multiplier_of(5)

print(times3(9)) # 27

print(times5(9)) # 45

# maja specjalny atrybut __closure__ ktory zwraca tuple

times3.__closure__[0].cell_contents