__author__ = 'INKQWIRE'

# Correct Version
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)


my_car = Car("DeLorean", "silver", 88)   #This is how instances should be created
print my_car.condition

print my_car.display_car()

# what I submitted
class Car(object):
    condition = "new"

    def display_car(self):
         return "This is a %s %s with %s MPG" % (self.color, self.model, str(self.mpg))

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

display_car = display_car(self, model, color, mpg)   #INCORRECT

model = "Delorean"
color = "silver"
mpg = 88

print display_car()