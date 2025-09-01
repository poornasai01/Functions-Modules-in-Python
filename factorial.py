n=int(input("Enter a number: "))
a="Factorial of "
b=" is: "
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(n)
n=str(n)
print(a+n+b,result)
