

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} make a sound"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} say meow"
    
class Bird(Animal):
    def speak(self):
        return f"{self.name} says chirp"
    
def make_animal_speak(animal):
    print(animal.speak())
    
ani = Animal("animal")
cat = Cat("mimi")
print(ani.speak())
print(cat.speak())
bird = Bird("jiji")
make_animal_speak(bird)


# 私有属性的封装
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age  # 私有属性

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

    def get_age(self):
        return self.__age

person = Person("Alice", 30)
print(person.get_name())  # 输出: Alice
person.set_age(35)
print(person.get_age())  # 输出: 35
# print(person.__age)  # 这行代码会报错，因为 __age 是私有属性

# 静态方法和类方法不依赖实例
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y

print(MathOperations.add(3, 5))  # 输出: 8
print(MathOperations.multiply(3, 5))  # 输出: 15
