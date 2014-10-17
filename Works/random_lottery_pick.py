import random
#
def lottery():
    random_pick = random.sample(range(36), 5)
    # return random_pick
    # for i in random_pick:
    #     print i
    i = 0
    i = i + 1
    while i < 100:
       return random_pick


lottery()

i = 0
x = 25
while i < x:
    i += 1
    print lottery()