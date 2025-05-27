class Vehicle:
    def start(self):
        print("Starting a normal vehicle engine")
        
class Car(Vehicle):
    def start(self):
        print("Starting a car engine using a key")
        
v=Vehicle()
c=Car()

v.start()
c.start()                