class Computer:

    def __init__(self, ram, gpu, processor):
        self.ram = ram
        self.gpu = gpu
        self.processor = processor

    def getspecs(self):
        print("Enter specifications")
        self.ram = input("Enter RAM size: ")
        self.gpu = input("Enter GPU model: ")
        self.processor = input("Enter PROCESSOR model: ")

    def displayspecs(self):
        print("Specifications of your system")
        print("Ram size:{} GPU:{} Processor:{}".format(self.ram, self.gpu, self.processor))


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_color(self):
        self.casecolor = input("Enter case color: ")

    def show_case_color(self):
        print("Desktop specifications")
        print("Case color:{}".format(self.casecolor))


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input("Enter weight: ")

    def show_weight(self):
        print("Laptop weight")
        print("Laptop weight:{}".format(self.weight))


object1 = Laptop("")
object1.getspecs()
object1.get_weight()
object1.displayspecs()
object1.show_weight