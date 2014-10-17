__author__ = 'INKQWIRE'

import random
#
def randon_array():
    random_pick = random.sample(range(1000), 10)
    # return random_pick
    # for i in random_pick:
    #     print i
    i = 0
    i = i + 1
    while i < 100:
       return random_pick


randon_array()

i = 0
x = 1000 # 10000 random number array
while i < x:
    i += 1
    print randon_array()