import random

def robin_miller_test(p, k=5):
  if p == 1:
    return False

  if p == 2:
    return True

  if(p%2 == 0):
    return False

  r,d = 0, p-1
  while d%2 == 0:
    r += 1
    d //= 2

  for _ in range(k):
    a = random.randint(2, p-2)
    x = pow(a, d, p)

    if x == 1 or x == p-1:
      continue

    for _ in range(r-1):
      x = pow(x,2,p)
      if x == p-1:
        break
    else:
      return False

  return True

P = 104729
if robin_miller_test(P, k=5):
  print(f"{P} is probably prime")
else:
  print(f"{P} is not prime")

