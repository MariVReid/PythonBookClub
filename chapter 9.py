#Chapter 9
class Rabbit:
    def __init__(self, name, age):
        self.name=name 
        self.age=age
        self.boxesDestroyed = 0
    def flop(self):
        print(f"{self.name} has flopped.")
    def dig(self):
        print(f"{self.name} is digging.")
    def destruct(self, count):
        self.boxesDestroyed = count + self.boxesDestroyed
    def boxes(self):
        print(f"{self.name} has destroyed {self.boxesDestroyed} boxes.")

my_rabbit = Rabbit('Gizmo', '3')
print(f"My bunny's name is {my_rabbit.name}, he is {my_rabbit.age} years old")
my_rabbit.flop()
my_rabbit.dig()
my_rabbit.boxes()

rabbit2 = Rabbit('Marlo', '5')
print(f"My bunny's name is {rabbit2.name}, she is {rabbit2.age} years old")
rabbit2.flop()
rabbit2.dig()
rabbit2.boxes()
rabbit2.boxesDestroyed= 8
rabbit2.destruct(2)
rabbit2.boxes()

class RabbitAdvanced(Rabbit):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed =  breed
    def getBreed(self):
        print(f"{self.name} belongs to the {self.breed} breed.")

rabbit3 = RabbitAdvanced('Domino', '8', "Holland Lop")
rabbit3.getBreed()

#You can store other classes into an atribute of a class. Then you can call functions from that class stored inside. (varName.insideclass.method())
#You can store classes in modules (another file) and then import them into the main file (from fileName import className). Then use as shown above (no dot notation)


