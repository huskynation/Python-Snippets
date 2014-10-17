
class Addition(object):                                         # built a class
    def sum_numbers(self):                                      # built method
        sum1 = raw_input("enter a number: ")                # takes first argument
        str(int(sum1))
        sum2 = raw_input("enter a second number: ")         # takes second argument
        str(int(sum2))
        sum_total = sum1+sum2                               # adds both numbers
        print sum_total                                     # prints total

sum = Addition()                                                # passes Class into sum variable
sum.sum_numbers()                                               # Calls method on a class