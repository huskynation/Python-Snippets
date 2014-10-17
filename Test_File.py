# def wadson():
#     name = raw_input("Please enter your name: ")
#     return name

# print wadson()

# from fractions import gcd

# x = gcd(20, 8)
# print x

#
# my_file = open("text.txt", "r+")
# myfile.write()
# i = 0
# while i < 4:
#     print my_file.readline()
# my_file.close()

class Car(object):
    condition = "new"
def __init__(self, model, color, mpg):
    self.model = model()
    self.color = color()
    self.mpg = mpg()

my_car = Car("Delorean", "silver", 88)

print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg