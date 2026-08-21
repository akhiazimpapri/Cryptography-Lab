import random

def lehmann_prime_test(p, k=20):
  if p == 1:
    return False

  if p == 2:
    return True

  if(p%2 == 0):
    return False


  a = random.randint(2, p-2)
  r = pow(a, p-1//2, p)
  if r == 1 or r == p-1:
    print(f"Composite witness found: a = {a}, r = {r}")
    return False

  return True


P = 231
if lehmann_prime_test(p, k=20):
  print(f"{p} is propably prime")
  print(f"probability score: {1-(1/2)**20}")

else:
  print("P is not prime")

