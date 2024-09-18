class Point:
    
    def __init__(self, x_loc, y_loc):
        self.x = x_loc
        self.y = y_loc

    def display(self):
        print("x:", self.x, "y:", self.y)

    def change_loc(self, x_new, y_new):
        self.x = x_new
        self.y = y_new


if __name__ == "__main__":
    point = Point(0, 0)
    point.display()
    point.change_loc(1, 2)
    point.display()
