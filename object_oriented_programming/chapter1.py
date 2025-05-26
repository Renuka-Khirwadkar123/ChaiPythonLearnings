class Car:
  
  total_car=0
  #__init__->constructor
  #self->keyword used to build telephone line between class attributes and object.
  #encapsulation->making attribute private
  def __init__(self,brand,model):
         self.__brand=brand
         self.__model=model
         #Car.total_car+=1
         self.total_car+=1
  def get_brand(self):
     return self.__brand + "!"

  def fullname(self):
     return f"{self.__brand} {self.__model}"
  def fuelType(self):
      return "Petrol or Diesel"
  @staticmethod
  def carmethod():
      return "Car are great mode of transport"
  @property
  def model(self):
      return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
         super().__init__(brand,model)
         self.batterysize=batterysize    
    def fuelType(self):
      return "Electric Charge"
# my_tesla=ElectricCar("Tesla","S","85KW")  
# print(my_tesla.get_brand())
# print(my_tesla.fuelType())

my_car=Car("Toyota","Corolla")
#my_car.brand
#my_car.model
#print(my_car.fullname())
#print(Car.total_car)
#print(my_car.total_car)
#print(my_car.carmethod())

# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

# cars=Car("Tata","Tiago")
# print(cars.carmethod())
# print(cars.model)
# print(isinstance(cars,Car))

class Battery:
    def battery_info(self):
      return "Returns Battery"

class Engine:
    def engine_info(self):
        return "Return Engine"
    

class ElectricCarTwo(Battery,Engine):
         pass

ec=ElectricCarTwo("b1","e1")
print(ec.battery_info())
    