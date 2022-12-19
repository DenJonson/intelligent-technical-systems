def evenNumbers():
  n = 0
  while True:
    yield n
    n += 2
    
g = evenNumbers()
for i in range(0, 10):
  print(next(g))