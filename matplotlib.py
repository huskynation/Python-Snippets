import numpy as np 
import matplotlib.pyplot as plt

xs = range(-100, 100, 10)
x2 = [x**2 for x in xs]
negx2 = [-x**2 for x in xs]
plt.plot(xs, x2)
plt.plot(xs, negx2)
plt.xlabel("x")
plt.ylabel("y")
ply.ylim(-2000, 2000)
plt.axhline(0)
plt.axvline(0)
plt.savefig("quad.png")
plt.show()