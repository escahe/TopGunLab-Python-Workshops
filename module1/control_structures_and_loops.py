from utils import word_spaces, input_request

"""TOP GUN LAB - Control Structures and Loops Excercises."""

def exercise1():
    """it prints the first ten numbers in the Fibonacci sequence"""
    print("** Control Structures and Loops - Exercise 1 first ten Fibo nums **")
    print("|  n  | fibo number |")
    print("="*21)
    nums = [0,1]
    this_fibo = 0
    for n in range(1,11):
        if n > 2:
            this_fibo = sum(nums)
            nums[0], nums[1] = nums[1], this_fibo
        else:
            this_fibo = n -1
        print(f"|{word_spaces(5,str(n))}|{word_spaces(13,str(this_fibo))}|")
    print("="*21)

def exercise2():
    """it asks you for a number by console and then
    prints if the number is prime or not"""
    print("** Control Structures and Loops - Exercise 2 is prime? **")
    number = input_request("Write a number: ", int)
    prime = True
    print_it = lambda prime: print(f'{number} is {"not " if not prime else ""}prime')
    if number < 2:
        print_it(not prime)
    else:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                print_it(not prime)
                break
        else:
            print_it(prime)
