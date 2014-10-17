__author__ = 'INKQWIRE'
principal = 1000    # Initial amount
rate = .05          # Interest Rate
numyears = 5        # Number of Years
year = 1
while year <= numyears:                     # If True executes the 3 lines below
    principal = principal * (1 + rate)
    print "%3d %0.2f" % (year, principal)   # Prints Year, then compounding value, formatted down to two decimals
    year = year + 1                         # Iteration


# print "%d", "%s", "%f" {Specifies the formatting structure of a...
    #...particular data type (string, integer, floating point, etc)}
