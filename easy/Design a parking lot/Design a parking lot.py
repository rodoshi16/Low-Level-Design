from __future__ import annotations
from typing import Optional
from enum import Enum
import threading

class Type(Enum):
    CAR = "car"
    TRUCK = "truck"
    VAN = "van"
    BIKE = "bike"

class Status(Enum):
    EMPTY = 'empty'
    OCCUPIED = 'occupied'

class Ticket:
    vehicle: Vehicle
    entry_time: int
    exit_time: Optional[int]
    price: int

    def __init__(self, vehicle, entry_time):
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.exit_time = None
        self.price = 0


class Vehicle:
    id: int
    type: str
    slot: ParkingSlot
    ticket: Ticket

    def __init__(self, id, t):
        self.id = id
        self.type = t
        self.slot = None
        self.ticket = None


class ParkingLot:
    HOURLY = 20
    levels: list[ParkingLevel]
    V: Vehicle

    def __init__(self, levels):
        self.levels = levels
    
    def park(self, V: Vehicle, time: int):
        for level in self.levels:
            slot = level.find_spot()
            if slot != -1:
                V.slot = slot
                t = Ticket(V, time)
                V.ticket = t
                return True
        return False
    
    def exit(self, V: Vehicle, time: int):
        V.ticket.exit_time = time
        V.ticket.price = (time - V.ticket.entry_time) * ParkingLot.HOURLY
        V.slot.status = Status.EMPTY
        V.slot.level.isFull = False

class ParkingLevel:
    level: ParkingLevel
    spots: ParkingSpot

    def __init__(self, level, spots):
        self.level = level
        self.spots = spots
        self.isFull = False
        self.lock = threading.Lock()
    
    def find_spot(self):
        with self.lock:
            for s in self.spots:
                if s.status == Status.EMPTY:
                    s.status = Status.OCCUPIED
                    return s
            self.isFull = True 
        return -1

class ParkingSpot:
    id: int
    level: int
    t: str
    status: str
    def __init__(self, id, level, t):
        self.id = id
        self.level = level
        self.type = t
        self.status = Status.EMPTY
