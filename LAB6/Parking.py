class ParkingSpot:

    def __init__ (self,spot_num,available,vechile_num):
        self.spot_num = spot_num
        self.available = available
        self.vechile_num = vechile_num

    def get_info(self):
        print(self.spot_num , self.available , self.vechile_num)


    def update_availability(self,status,vechile_num):
        self.available = status
        self.vechile_num = vechile_num

if __name__ == '__main__':
    parking = ParkingSpot(15,True,None)
    parking.get_info()
    parking.update_availability(False,'QBQ -4533')
    parking.get_info()