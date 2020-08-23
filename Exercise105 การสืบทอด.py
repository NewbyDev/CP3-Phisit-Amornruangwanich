class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    pass
class Car(Vehicle):
    pass
class van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

Pickup1 = Pickup()
Pickup1.turnOnAirConditioner()

Car1 = Car()
Car1.turnOnAirConditioner()

van1 = van()
van1.turnOnAirConditioner()

EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()