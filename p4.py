#multi-level inheritance
class Animal:
    def run(selfself):
        print("Animals run")
class Dog(Animal):
    def bark(selfself):
        print("dog barks")
class Puppy(Dog):
    def drink(selfself):
        print("puppy drinks milk")
p=Puppy()
p.drink()
p.bark()
p.run()

#multiple inheritance
class ArithmeticOperation1:
    def Addition(self, i, j):
        return i + j


class ArithmeticOperation2:
    def Multiple(self, i, j):
        return i * j


class Derived(ArithmeticOperation1, ArithmeticOperation2):
    def Subtract(self, i, j):
        return i - j

d = Derived()
print(d.Addition(5,6))
print(d.Multiple(5, 6))
print(d.Subtract(6, 5))