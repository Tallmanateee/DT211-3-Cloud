''' This code solution is taken from Paul Doyle's video on Nitrous and is for the first euler challenge'''

n=0
for i in xrange(1,1000):
  if not i % 5 or not i % 3:
    n = n + i

print n