class Booking:
    vehicle="Car"  #class variable
    def details(self,timeperiod,place):  #Instance variable
        self.timeperiod=timeperiod
        self.place=place
        return f"Trip to {self.place} for {self.timeperiod} days"

    #Change Vehicle type
    @classmethod
    def change_vehicle(cls,new_vehicle):
         cls.vehicle=new_vehicle


Booking.change_vehicle("Bike")
b1=Booking()
print(b1.vehicle)
print(b1.details(3,"Kerala"))