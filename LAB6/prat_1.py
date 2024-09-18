class ComplexNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def change_real(self, new_real):
        self.real = new_real

    def change_img(self, new_imaginary):
        self.imaginary = new_imaginary

    def get_real(self):
        return self.real
    
    def get_img(self):
        return self.imaginary
    
    def absolute(self):
        z = (((self.real)**2) + ((self.imaginary)**2))**(0.5)
        print(z)
    
    def to_string(self):
        print(f"{self.real}+i{self.imaginary}")

def complex_add(cx_num1, cx_num2):
    real_sum = cx_num1.get_real() + cx_num2.get_real()
    imaginary_sum = cx_num1.get_img() + cx_num2.get_img()
    return ComplexNum(real_sum, imaginary_sum)

if __name__ == '__main__':
    comp_n1 = ComplexNum(4, 5)
    comp_n2 = ComplexNum(2, 3)
    comp_n3 = complex_add(comp_n1, comp_n2)
    comp_n3.to_string()

#    complexnum = ComlexNum(4,5)
#    complexnum.to_string()
#    complexnum.absolute()
#    complexnum.change_img(6)
#    complexnum.to_string()
#    complexnum.absolute()
    