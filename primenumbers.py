num = int(input("Enter the number you want to check if its prime or not: "))
def prime(num):
    temp = 0
    for i in range(2, int(num**1/2 + 1)):
        if num < 2:
            return "Enter num greater than 2"
            
        if num%2 == 0 and num%num**1/2 == 0:
            return "Num is not Prime"
        else:
            return "Num is Prime"
print(prime(num))