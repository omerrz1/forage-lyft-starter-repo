from datetime import datetime,timedelta
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        four_years = timedelta(days=365*4)
        return self.current_date - self.last_service_date >= four_years
