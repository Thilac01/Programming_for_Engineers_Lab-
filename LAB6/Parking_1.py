class ParkingSpot:
    
    def __init__(self, spot_num, available, vehicle_num):
        self.spot_num = spot_num
        self.available = available
        self.vehicle_num = vehicle_num

    def get_info(self):
        return f"Spot Number: {self.spot_num}, Available: {self.available}, Vehicle Number: {self.vehicle_num}"

    def update_availability(self, status, vehicle_num):
        self.available = status
        self.vehicle_num = vehicle_num

if __name__ == '__main__':
    parking_spots = {
        1: ParkingSpot(1, True, None),
        2: ParkingSpot(2, True, None),
        3: ParkingSpot(3, True, None),
        4: ParkingSpot(4, True, None),
        5: ParkingSpot(5, True, None)
    }


    for spot in parking_spots.values():
        print(spot.get_info())

    parking_spots[2].update_availability(False, 'QBQ-4533')

    print("\nAfter update:")
    for spot in parking_spots.values():
        print(spot.get_info())
