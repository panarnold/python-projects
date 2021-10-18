#operator overloading: te same operacje daja inny behawior dla obiektów innych klas
#wbudowane funkcjonalnosci pythona mają taką konwencję nazwy, ze daje sie double underscory do nich
# np __len__() koresponduje do len(), a __add__() do operatora '+'

# z defaulta, wiekszosc wbudowanych funkcji i operatorow nie bedzie pracowala z obiektami moich klas
# trzeba te metody dodac, zeby byly kompatybilne

#dlatego len() jest rownoznaczne z obj.__len__() , a a[0] rownoznaczne z a.__getitem__(0)
# jak wpisze sie dir(obj), mamy liste funkcji ktore wspiera: wbudowane i te doslowne, a oprocz tego wlasciwosci

#overloading

class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart) #przy overloadingu tej samej funkcji musi zwracac domyslnie to samo, inaczej TypeError

    def __bool__(self):
        return len(self.cart) > 0 

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __iadd__(self, other): #chodzi o +=
        self.cart.append(other)
        return self # ale gdyby byl return 'HEY DUPA', to overload tej funkcji by był

    def __getitem__(self, key):
        return self.cart[key]

    def __radr__(self, other):
        new_cart = self.cart.copy()
        new_cart.insert(0, other)
        return Order(new_cart, self.customer)

order = Order(['dupa','kał','mors'], 'Arnold')
len(order)

#interpretacja abs - absolute value of vector

class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __abs__(self):
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5


    def __str__(self):
        return f'{self.x_comp}i{self.y_comp:+}j'

    #__repr__ : parsable representation of an object

    def __repr__(self):
        return f'Vector({self.x_comp}, {self.y_comp})'

    
# __str__

# complete example

from math import hypot, atan, sin, cos

class CustomComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, self.imag) #ekwiwalent od CustomComplex(real, imag)
    
    def argz(self):
        return atan(self.imag / self.real)

    def __abs__(self):
        return hypot(self.real, self.imag)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.real}, {self.imag})'
    
    def __str__(self):
        return f'({self.real}{self.imag:+}j)'

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag

        if isinstance(other, CustomComplex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag

        return self.__class__(real_part, imag_part)

    

