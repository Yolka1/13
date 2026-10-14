class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octopus:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octopus = Octopus()

print (bear.eats())
print (rabbit.eats())
print (octopus.eats())


class Laser:
    def does(self):
        return 'disigntegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.smartphone.does())

robot = Robot()
robot.does()