#To find prime factors of a number

number = int(input("Enter the number you want to get prime factors of: "))

def prime(n):
  
  if n <= 1:
    return False
  for i in range (2, int(n**0.5) + 1):
    if n % i == 0:
        return False
  return True
      

def natural(number):
  list2 = []
  for f in range(2, number + 1):
    list2.append(f)
  return list2

def prime_factors(number):
  primes  = [i for i in natural(number) if prime(i)]
  factors = []

  for p in primes:
    while number % p ==0:
      factors.append(p)
      number //= p   

  return factors 

result = prime_factors(number)
print("Prime factors:", " x ".join(map(str, result)))
