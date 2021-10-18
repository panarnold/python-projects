# inheritance: dziedziczy, rozszerza, czerpie (derive) np Horse IS Animal

# composition: relacja 'has' CompositeClass HAS a ComponentClass, Horse HAS a Tail
#composition umozliwia reuzywanie kodu przez dodawanie ich do innych obiektów


#wszystko w python jest obiektem: moduły, definicje klas i funkcji są obiektami, obiekty z klas też

#kazda klasa w python derives from object

#wszystkie klasy czerpią z object, poza exceptionami - bo te czerpią z BaseException

# BaseException provides, dlatego errory deriwujemy tak:

class MyError(Exception):
    pass

raise MyError()

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('calculating payroll')
        print('====================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- check amount: {employee.calculate_payroll()}')
            print('')





#w takim wypadku lepiej robić interfejsy czy klasy abstrakcyjne
# klasy abstrakcyjne istnieją, by z nich dziedziczyc, lecz by ich nie instajcjować

# underscore, ale raczej abc module

from abc import ABC, abstractmethod

class Employeee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod #pokazuje ze TRZEBA nadpisać
    def calculate_payroll(self):
        pass


# nowoczesne języki pozwalają dziedziczyc z jednej klasy, ale implementować wiele interfejsów

# w pythonie nie trzeba explicitnie deklarować interfejsów tylko tzw 'duck typing' -> jesli zachowuje sie jak kaczka, jest to kaczka np

class DisgruntledEmployee(self, id, name):
    self.id = id
    self.name = name

    def calculate_payroll(self):
        return 10000 # nie derivuje z Employee, ale spelnia te same wymagania do Payroll System

#def calculate_payroll(self, employees):
        # print('calculating payroll')
        # print('====================')
        # for employee in employees:
        #     print(f'Payroll for: {employee.id} - {employee.name}')
        #     print(f'- check amount: {employee.calculate_payroll()}')
        #     print('')
            # wymaga: listy obiektów, które implementuja id, name, 

# dlaczego nie inheretencja? np Customer moze miec id i name, tak jak Employee, ale nie moga dziedziczyc z jednego, dlatego interfejs
# jesli klasa ma byc reused -> implementuj interfejs



import productivity, hr, employees

manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kurwa Jebana', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Adam Małysz', 40, 9)

employees = [manager, secretary, sales_guy, factory_worker, temporary_secretary]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)

#program działa, 

#kompozycja: kompozyt składający się z komponentów







