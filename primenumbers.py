num = int(input("Enter the number you want to check if its prime or not: "))
def prime(num):
    for i in range(2, int(num**1/2 + 1)):
        if num < 2:
            return "Enter num greater than 2"
            
        if num%i==0:
            return False
    return True

a = prime(num)
if a == True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")