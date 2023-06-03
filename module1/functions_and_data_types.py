from utils import input_request
"""TOP GUN LAB - Functions and Data Types."""

def exercise1():
    """it asks you for a list of numbers by console and then
    prints the maximum number from the list"""
    print("** Functions and Data Types - Exercise 1 maximum number **")
    numbers = input_request("Write numbers separated by non-numeric characters:\n", list)
    print(f"The maximum number in {numbers} is: {max(numbers)}")

def exercise2():
    """it asks you for a text by console and then
    prints that text reversed"""
    print("** Functions and Data Types - Exercise 2 reversed string **")
    text = input("Write a text: ")
    print(f"'{text}' reversed is '{text[::-1]}'")
