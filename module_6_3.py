class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx*self.speed
        self.dy = dy*self.speed
        self.dz = dz * self.speed
        if self.dz < 0:
            print("It's too deep, i can't dive :(")


    def get_cords(self):
        print(f' X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        if Animal._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif Animal._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    import random
    beak = True
    def lay_eggs(self):
        print(f'Here are(is) {self.random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = abs(self.dz-dz*(self.speed/2))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    #super().__init__()
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()