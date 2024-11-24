ask_user = int(input("Enter the number you want factorial of: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(f"The factorial of the {ask_user} is ",factorial(ask_user))
    