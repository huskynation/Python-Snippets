   for x in range(2, n):
      if n % x == 0:
        print("{} equals {} x {}".format(n, x, n // x))
        return False
   else:
      print(n, "is a prime number")
      return True