class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', self 
    
    @staticmethod 
    def staticmethod():
        return 'static method called' #tylko tutaj bez self i slowa kluczowego

obj = MyClass()
print(obj.method())

#class methods mozna uzyc jako factory functions:
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}) 'f'{self.ingredients!r}')

    @classmethod
    def margherita(cls):
        return cls(['mozarella','tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozarella','tomatoes','ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi