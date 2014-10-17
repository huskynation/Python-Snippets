__author__ = 'INKQWIRE'
import time
a = [i for i in range(1000000)]
# print a
sum = 0
t1 = time.time()
for i in a:
    sum = sum + i
    # print i
t2 = time.time()
print t2-t1‰