import time, random

"""TOP GUN LAB - Programming Best Practices."""
def exercise1():
    """it asks you for a word then checks if the word is a palindrome
    by calling is_palindrome function."""
    word = None
    while not word:
        word = input("write a word: ")
        try:
            result = is_palindrome(word)
            print(f"{word} is {'' if result else 'not '}a palindrome")
        except Exception as e:
            word = None
            print(e)

def exercise2():
    """calls the sort numbers function that is decorated with @timer
    to check how long it takes to execute
    """
    numbers = [random.randint(1,100) for _ in range(10)]
    sort_numbers(numbers)

def is_palindrome(word:str)->bool:
    if not isinstance(word, str):
        raise TypeError("only string allowed")
    if not word.isalpha():
        raise ValueError("Only alphabetic chars allowed")
    lower_word = word.lower()
    return lower_word == lower_word[::-1]

def timer(func):
    """Decorator that measures the time taken to execute a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time*1000} milliseconds")
        return result
    return wrapper

@timer
def sort_numbers(numbers:list):
    """it receives a list of numbers then sorts and prints it"""
    print("*"*11," Unsorted list ","*"*11)
    print(numbers)
    sorted_numbers = sorted(numbers)
    print("*"*12," Sorted list ","*"*12)
    print(sorted_numbers)
    print("*"*39)
