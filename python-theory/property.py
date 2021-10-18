#mozna tak, a mozna przez dekorator, i dekorator niby lepiej
# parametry opcjonalne property(fget, fset, fdel, doc)

class Person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        self.__name = name
        print('setname() called')
    
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name

    name = property(getname, setname, delname)

p1 = Person()
p1.name='Steve'

del p1.name

class Dupsko:
    def __init__(self):
        self.__name=''
    
    @property
    def getname(self): return self.__name

#uzycie getterów i setterów z @property

class Celcius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32


human = Celcius()
human.temperature = 37

#tak wygladaja gettery i settery bez tego
print(human.temperature)
#dostep do funkcji
print(human.to_farenheit())

print(human.__dict__)

#dlatego trzeba tak

class Celcius:
    def __init__(self, temperature = 0):
        self.temperature = temperature 

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

    @property # TAK GO TWORZYMY!!!!!!!
    def temperature(self):
        print('Getting value')
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        print('setting value')
        if value < -273.15:
            raise ValueError('Temperature below -273 is not possible')
        self.__temperature = value

huj = Celcius(37)

