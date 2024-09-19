class ParkingSpot:
    
    def __init__ (self, spot_num, available, vehicle_num):
        self.spot_num = spot_num
        self.available = available
        self.vehicle_num = vehicle_num

    def get_info(self):
        if self.available:
            print(f"Spot {self.spot_num}: Available")
        else:
            print(f"Spot {self.spot_num}: Occupied by {self.vehicle_num}")

    def update_availability(self, status, vehicle_num):
        self.available = status
        self.vehicle_num = vehicle_num

if __name__ == '__main__':
    parking = ParkingSpot(15, True, None)
    parking.get_info()  
    parking.update_availability(False, 'QBQ -4533')
    parking.get_info()  
