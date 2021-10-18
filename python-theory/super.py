# extends funcionality of classes

# single inheritance

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

# to extend funcionality

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

#jesli sie niczym nie rozni jak np Square od Cube, to mozna skipowac super().__init__(), bo wykonuje sie automatycznie

# deeper dive
# super() moze wziac super(class, instance), odwolujac sie do konkretnego obiektu. w wypadku braku multiinheritance znaczy to samo co

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs) #pozwala userowi instanowanie obiektow tylko z argumentami, dlatego mozemy zrobic pyramid = RightPyramid(base=2, slant_height=4)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
    
    def area_2(self):
        base_area = super().area()
        trainge_area = super().tri_area()
        return trainge_area * 4 + base_area
        

    #o kolejnosci decyduja Method Resolution Order. kazda klasa ma __mro__ zeby sprawdzic ten order
        
    