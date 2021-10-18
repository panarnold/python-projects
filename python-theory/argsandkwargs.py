#pozwalają dodać x argumentów do funkcji, więc nie musisz wiedzieć ile argumentów podać

#przekazują unkeyworded zliste argumentów

#nie trzeba tych nazw, ale warto zachować konwencje

#ARGS
def test_var_args(f_arg, *argv):
    print('first normal arg:', f_arg)
    for arg in argv:
        print('another arg through *argv:', arg)

test_var_args('dupa', 'lukasz', 'jan', 'kał')

print('\n***\n')

#KWARGS
#dla keyworded 

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="andrzej")

print('\n***\n')

#uzywanie args i kwargs do wezwania funkcji

def another_test(arg1,arg2,arg3):
    print('arg1:', arg1);
    print('arg2:', arg2);
    print('arg3:', arg3);

args = ('two', 3, 5)

another_test(*args)

print('\n***\n')

kwargs = {'arg3': 3, 'arg2': 'two', 'arg1': 5}
another_test(**kwargs)

print('\n***\n')

#order of using: some_func(fargs, *args, **kwargs)

#KIEDY UŻYWAMY?
#Nnajczęściej przy dekoratorach funkcji
# przy monkey-patching (modyfikowanie kodu podczas runtime)