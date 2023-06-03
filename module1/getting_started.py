from utils import input_request
"""TOP GUN LAB - Getting Started With Python Excercises."""
def exercise1():
    """it asks you for two numbers through the console
    then it prints the sum of both"""
    print("** Getting Started - Exercise 1 SUM **")
    number_1 = input_request("Write first number: ")
    number_2 = input_request("write second number: ")
    print(f"Result:\n{number_1} + {number_2} = {number_1 + number_2}")

def exercise2():
    """it asks you for a tempeture in Fahrenheit through the console
    then it prints the equivalent in Celsius"""
    print("** Getting Started - Exercise 2 °F to °C **")
    temp_F = input_request("Write the temperature in °F : ", float)
    temp_C = round((temp_F - 32) * 5/9, 2)
    print(f"Result:\n{temp_F} °F = {temp_C} °C")
