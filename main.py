from utils import word_spaces,input_request, Alignment
from module1 import getting_started, control_structures_and_loops, functions_and_data_types, advanced_python_concepts, programming_best_practices
import sys, os

def main():
    selection = None
    message = ""
    while not selection:
        os.system("clear")
        print_menu()
        if message:
            print("Warning: ", message)
            message = ""
        selection = input_request("Write the number of your choice: ")
        if selection < 1 or selection > 11:
            message = f"{selection} is not a valid option"
            selection = None
            continue
        while True:
            os.system("clear")
            options.get(selection, sys.exit)()
            if "y" not in input("Do you want to try again (y/n)?").lower():
                selection = None
                break

def print_menu():
    header = "*"*20 + " Menu " + "*"*20
    len_header = len(header)
    print(header)
    print("*"*len_header)
    for n, option in options.items():
        print(f"* {word_spaces(len_header-4, f'[{n}] '+option.__module__[8:]+' '+ option.__name__, Alignment.LEFT)} *")
    print(f"* {word_spaces(len_header-4, '[11] Exit', Alignment.LEFT)} *")
    print("*"*len_header)

options = {
    1: getting_started.exercise1,
    2: getting_started.exercise2,
    3: control_structures_and_loops.exercise1,
    4: control_structures_and_loops.exercise2,
    5: functions_and_data_types.exercise1,
    6: functions_and_data_types.exercise2,
    7: advanced_python_concepts.exercise1,
    8: advanced_python_concepts.exercise2,
    9: programming_best_practices.exercise1,
    10: programming_best_practices.exercise2
}

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n"+"="*53,"\n| Program interrupted, thanks for checking this out |\n","="*53)