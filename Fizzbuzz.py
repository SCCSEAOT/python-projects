#FizzBuzz!

fizz = 3
buzz = 5

for num in range(101):
    if num % fizz == 0 and num % buzz == 0:
        print("FizzBuzz!")
    elif num % buzz == 0:
        print("Buzz")
    elif num % fizz == 0:
        print("Fizz")
    else:
        print(num)
