# class Car(object):
#     condition = "new"
# def __init__(model, color, mpg):
#     self.model = model
#     self.color = color
#     self.mpg = mpg

# model = "Delorean"
# color = "silver"
# mpg = 88

# my_car = Car()
# print my_car.condition

class Car(object):
    condition = "new"
    
    def display_car(self, model, color, mpg):
         return "This is a %s %s with %s MPG" % (self.color, self.model, str(self.mpg)) 

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

display_car = display_car(self, model, color, mpg)
        
model = "Delorean"
color = "silver"
mpg = 88

print display_car()

