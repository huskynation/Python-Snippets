def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

import random
random_number = random.sample(range(100), 25)


print random_number                             # Prints unsorted list

sorted = qsort1(random_number)                  # applies qsort algo
for x in sorted: print x                        # prints out sorted list