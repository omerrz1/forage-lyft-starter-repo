from datetime import datetime,timedelta
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        Three_years = timedelta(days=365*3)
        return self.current_date - self.last_service_date >= Three_years

           