import string

for x in range(1, 11):
   print string.rjust('x', 2), string.rjust('x*x', 3),
   # Note trailing comma on previous line
   print string.rjust('x*x*x', 4)

for x in range(1,11):
   print'%2d %3d %4d' % (x, x*x, x*x*x)
