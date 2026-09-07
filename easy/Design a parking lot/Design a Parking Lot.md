***Parking Lot System***

Requirements:

- n number of slots (size) and m levels
- accomodate diff vehicles (cars, bike, truck, vans etc) 
- payment system (to pay for parking) based on number of hours a car can be parked
system should track availability of slots and provide real time information to customers. 

classes and objects:

- ParkingLot, ParkingSpot, Vehicle, ParkingLevel

- ParkingLot:
* self.levels = [Level Objects]
* list of parking lot slots
* park(Vehicle): loop through levels and check which is not full, call level.find_spot
* exit(vehicle): free the data structure - change the status and isFull to False


ParkingLevel:

- init: (level number, self.spots: []), self.full = False
- find_spot(): iterate through all spots and find status is available and return spot, isFull is set to True

- ParkingSpot:

* level, type, size, status, id


- Vehicle:

* Id, type, parking_slot


