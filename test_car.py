import unittest
from datetime import date
from unittest.mock import MagicMock

from car_factory import CarFactory
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine  
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery  
from battery.nubbin_battery import NubbinBattery
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

class TestCarFactory(unittest.TestCase):

    def test_create_calliope(self):
        current_date = date(2023, 8, 10)
        last_service_date = date(2023, 7, 1)
        current_mileage = 1000
        last_service_mileage = 800
        sensors = MagicMock()
        
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensors)
        
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertIsInstance(car.tires, Carrigan)

    def test_create_glissade(self):
        current_date = date(2023, 8, 13)
        last_service_date = date(2023, 6, 15)
        current_mileage = 1200  
        last_service_mileage = 1000
        sensors = MagicMock()

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensors)
        
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertIsInstance(car.tires, Octoprime)

    def test_create_palindrome(self):
        current_date = date(2023, 8, 11)
        last_service_date = date(2023, 7, 4)
        warning_light_on = True
        sensors = MagicMock()
        
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on, sensors)
        
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertIsInstance(car.tires, Carrigan)

    def test_create_rorschach(self):
        current_date = date(2023, 8, 15) 
        last_service_date = date(2023, 7, 10)
        current_mileage = 1100
        last_service_mileage = 900
        sensors = MagicMock()
        
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensors)
        
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertIsInstance(car.tires, Octoprime)

    def test_create_thovex(self):
        current_date = date(2023, 8, 17)
        last_service_date = date(2023, 6, 20)
        current_mileage = 1300
        last_service_mileage = 1100
        sensors = MagicMock()
        
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensors)
        
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertIsInstance(car.tires, Octoprime)
        
class TestCar(unittest.TestCase):

    def test_needs_service_engine_true(self):
        # Arrange
        engine = MagicMock()
        engine.needs_service.return_value = True
        
        battery = MagicMock()
        battery.needs_service.return_value = False
        
        tires = MagicMock()
        tires.needs_service.return_value = False
        
        car = Car(engine, battery, tires)
        
        # Act
        result = car.needs_service()
        
        # Assert
        self.assertTrue(result)

    def test_needs_service_battery_true(self):
        # Arrange 
        engine = MagicMock()
        engine.needs_service.return_value = False
        
        battery = MagicMock()
        battery.needs_service.return_value = True
        
        tires = MagicMock()
        tires.needs_service.return_value = False
        
        car = Car(engine, battery, tires)
        
        # Act
        result = car.needs_service()
        
        # Assert
        self.assertTrue(result)

    def test_needs_service_tires_true(self):
       # Arrange
        engine = MagicMock()
        engine.needs_service.return_value = False
        
        battery = MagicMock()
        battery.needs_service.return_value = False
        
        tires = MagicMock()
        tires.needs_service.return_value = True
        
        car = Car(engine, battery, tires)
        
        # Act 
        result = car.needs_service()
        
        # Assert
        self.assertTrue(result)

    def test_needs_service_all_false(self):
        # Arrange
        engine = MagicMock()
        engine.needs_service.return_value = False
        
        battery = MagicMock()
        battery.needs_service.return_value = False
        
        tires = MagicMock()
        tires.needs_service.return_value = False
        
        car = Car(engine, battery, tires)
        
        # Act
        result = car.needs_service()
        
        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()