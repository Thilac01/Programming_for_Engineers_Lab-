class Point:

    def __init__(self,x_loc,y_loc):
        self.x = x_loc
        self.y = y_loc

    def display(self):
        print("x" , self.x ,"y",self.y)

if __name__ == "__main__":
    point = Point(0,0)
    point.display()
