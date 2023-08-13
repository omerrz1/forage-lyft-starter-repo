from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self,sensors):
        self.sensors = sensors

    def needs_service(self):
        for sensor in self.sensors:
            if sensor >=0.3:
                return True
            else:
                return False
