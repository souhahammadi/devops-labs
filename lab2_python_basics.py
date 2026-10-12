import copy
def title(text):
    print("\n" + "=" * 10, text, "=" * 10)


title("2.2.1.1 Data Type: Numerics")
print(True + False)       
print(True or False)      
print(5 // 2)            
print(5 % 2)              
print(3 ** 2)             
print(5 + 1.6)           


title("2.2.1.2 Data Type: Strings")
S = 'python'
print(len(S))                       
print(S[0], S[1], S[-1])           
print(S + '1', S * 2)               


try:
    S[0] = 'Z'                      
except TypeError as e:
    print("Exception:", e)
S1 = 'Z' + S[1:]
print("S:%s,S1:%s" % (S, S1))       


S = "python"
print(S.split('h'))                 
print(S.replace('py', 'PY'))        
print(S.upper())                    
print('PYTHON'.lower())             
line = 'aa,bb,ccc,dd\n'             
print(repr(line))
print(' '.join(['life', 'is', 'short']))   
hw12 = '%s %s %d' % ('hello', 'world', 12)
print(hw12)                         


title("2.2.1.3 Data Type: Lists")
animals = ['cat', 'dog', 'monkey']
animals.append('fish')
print(animals)                      
animals.remove('fish')
print(animals)                      
animals.insert(1, 'fish')
print(animals)                      
animals.pop(1)
print(animals)                      

for i in enumerate(animals):        
    print(i)

squares = [x * 2 for x in animals]  
print(squares)                      

list1 = [12, 45, 32, 55]
list1.sort()
print(list1)                        
list1.reverse()
print(list1)                        


title("2.2.1.4 Data Type: Tuples")
T = (1, 2, 3)
print(T + (4, 5))                   
t = (42,)                          
print(t, type(t))
tuple1 = (12, 45, 32, 55, [1, 0, 3])
try:
    tuple1[0] = "good"              
except TypeError as e:
    print("Exception:", e)
tuple1[4][0] = 2                   
print(tuple1)                       


title("2.2.1.5 Data Type: Dictionaries")
x = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
x = dict(food='Spam', quantity=4, color='pink')
x = dict([("food", "Spam"), ("quantity", "4"), ("color", "pink")])
x = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

d = x.copy()
d['color'] = 'red'
print(x)                           
print(d)                            

try:
    print(d['name'])                
except KeyError as e:
    print("KeyError:", e)
print(d.get('name'))                
print(d.get('name', 'The key value does not exist.'))
print(d.keys())
print(d.values())
print(d.items())
d.clear()
print(d)                            
del d


title("2.2.1.6 Data Type: Sets")
sample_set = {'Prince', 'Techs'}
print('Data' in sample_set)         
sample_set.add('Data')
print(sample_set)
print(len(sample_set))              
sample_set.remove('Data')
print(sample_set)                   

list2 = [1, 3, 1, 5, 3]
print(list(set(list2)))             
sample_set = frozenset(sample_set)  
print(sample_set)


title("2.2.2 Deep Copy and Shallow Copy")
Dict1 = {'name': 'lee', 'age': 89, 'num': [1, 2, 8]}
Dict_copy = Dict1.copy()            
Dict_dcopy = copy.deepcopy(Dict1)   
Dict2 = Dict1                       
Dict1['num'][1] = 6                 
print('Dict1:' + str(Dict1) + "\n", 'Dict_copy:' + str(Dict_copy) + "\n",
      'Dict_dcopy:' + str(Dict_dcopy) + "\n", 'Dict2:' + str(Dict2))

title("2.2.3 if Statement")


def score_level(score):
    try:
        score = float(score)
        if 100 >= score >= 90:
            print(score, "-> Excellent")
        elif 90 > score >= 80:
            print(score, "-> good")
        elif 80 > score >= 60:
            print(score, "-> medium")
        elif 60 > score >= 0:
            print(score, "-> bad")
        else:
            raise ValueError
    except Exception:
        print(score, "-> Enter a correct score.")



for s in ["95", "85", "70", "30", "150", "abc"]:
    score_level(s)


title("2.2.4 Loop Statement - for loop (multiplication table)")
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %2d" % (i, j, i * j), end=" \t ")
    print()

title("2.2.4 Loop Statement - while loop")
i = 0
while i < 9:
    i += 1
    if i == 3:
        print("End the current loop.")
        continue
    if i == 5:
        print("End the current big loop.")
        break
    print(i)


title("2.2.5 Customizing Functions")


def Print_Hello():
    print("Hello, Python.")


Print_Hello()


def hello(greeting='hello', name='world'):
    print('%s, %s!' % (greeting, name))


hello()                            
hello('Greetings')                 
hello(name='Huawei')                
hello('Greetings', 'universe')     


def test(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


test(1, 2, 3, 4, 5, 6, x=10, y=11)


def plus_one(number):
    return int(number) + 1


print(plus_one(10))                 


title("2.2.6 I/O Operations")
f = open("text.txt", 'w')
Str = "Python file operation"
f.write(Str)
f.close()


f = open("text.txt", 'r')
print(f.read(6))                    
print(f.read())                     
f.close()


with open("text1.txt", 'w') as f:
    f.write("python file operation")
with open("text1.txt", 'r') as f:
    print(f.read())


title("2.2.7 Exception Handling")
try:
    print('The first number divided by the second number is %f' % (int("10") / int("0")))
except ZeroDivisionError:
    print('The second digit cannot be 0.')


try:
    print('The first number divided by the second number is %f' % (int("hello") / int("0")))
except Exception as result:
    print('Captured exception: %s' % result)

for a, b in [("10", "2"), ("10", "0")]:
    try:
        r = int(a) / int(b)
    except ZeroDivisionError:
        print("Code with exception: division by zero")
    else:
        print("Code without exception:", r)
    finally:
        print("Code executed at last, regardless of exception")

title("2.2.8.1 Creating and Using Classes")


class Dog1():
    def sit(self):
        print("Dog is now sitting")

    def roll_over(self):
        print("Dog rolled over!")


dog = Dog1()
dog.name = "Husky"
dog.sit()
dog.roll_over()
print(dog.name)

title("2.2.8.2 Attributes of Class (__init__)")


class Dog2():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is now sitting")

    def roll_over(self):
        print(self.name + " rolled over!")


dog = Dog2("Husky", 2)
print(dog.age)
dog.sit()
dog.roll_over()

title("2.2.8.3 Encapsulating Classes (private attribute)")


class Dog3():
    def __init__(self, name, age):
        self.name = name
        self.__age = age            

    def get_age(self):
        return self.__age


dog = Dog3("Husky", 2)
print(dog.name)
print(dog.get_age())                
try:
    print(dog.__age)                
except AttributeError as e:
    print("AttributeError:", e)

title("2.2.8.4 Inheriting Classes")


class Husky(Dog3):
    pass


mydog = Husky('Larry', 3)
print(mydog.name)                  
print(mydog.get_age())              

title("2.2.8.5 Class Polymorphism")


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def shout(self):
        print('Dog shouts')


class Husky2(Dog):
    def shout(self):
        print('woo')


class Tibetan_Mastiff(Dog):
    def shout(self):
        print('barking')


def sound(dog):
    dog.shout()


sound(Husky2('Larry', 3))           
sound(Dog('Richard', 2))            
sound(Tibetan_Mastiff('Sylvia', 4)) 
