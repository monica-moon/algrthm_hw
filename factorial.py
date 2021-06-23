
def factorial(n):
    result = 1


    if n != 0:
       for i in range(1, n +1):
        result *= i
    print(f'factorial of {n} is {result}')



number = int(input('Input number :'))
factorial(number)