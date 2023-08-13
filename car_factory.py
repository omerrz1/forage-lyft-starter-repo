from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime
from car import Car


class CarFactory():
    
    @classmethod
    def  create_calliope(cls,current_date, last_service_date, current_mileage,last_service_mileage,sensors):
        # create the car's engine
        cls.engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        # create the car's battery 
        cls.battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        # create car's tires
        cls.tirs = Carrigan(sensors=sensors)
        # create and return the car its self
        return Car(engine=cls.engine,battery=cls.battery,tires=cls.tirs)
    
    @classmethod
    def create_glissade(cls,current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        cls.engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        cls.battery = cls.battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        cls.tires = Octoprime(sensors=sensors)

        return Car(engine=cls.engine,battery=cls.battery,tires=cls.tires)
    
    @classmethod
    def create_palindrome(cls,current_date, last_service_date, warning_light_on,sensors):
        cls.engine= SternmanEngine(warning_light_is_on=warning_light_on)
        cls.battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        cls.tires = Carrigan(sensors=sensors)

        return Car(engine=cls.engine,battery=cls.battery,tires=cls.tires)
    
    @classmethod
    def create_rorschach(cls,current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        cls.engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        cls.battery = NubbinBattery(last_service_date=last_service_date,current_date=current_date)
        cls.tires = Octoprime(sensors=sensors)

        return Car(engine=cls.engine,battery=cls.battery,tires=cls.tires)

    
    @classmethod
    def create_thovex(cls,current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        cls.engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        cls.battery = NubbinBattery(last_service_date=last_service_date,current_date=current_date)
        cls.tires = Octoprime(sensors=sensors)

        return Car(engine=cls.engine,battery=cls.battery,tires=cls.tires)