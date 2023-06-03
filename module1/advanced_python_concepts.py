import sys, os, random, re
from utils import word_spaces, input_request

"""TOP GUN LAB - Advanced Python Concepts."""
def exercise1():
    """it creates a bank account with $0 balance
    you are able to deposit, withdraw and check balance"""
    BankMenu()

def exercise2():
    """it asks you for a .txt file path then it prints 
    the occurrences of each word in that text file"""
    print("** Advanced Python Concepts - Exercise 2 word occurrences in a txt file **")
    print("Notes:\n* If the file is at the same module1.py level just write the file name")
    print("* If you don't write any path or the file doesn't exist, a default text will be taken")
    path = input("Write a txt file path/name (e.g. MyText.txt or C/folder/MyText.txt):\n")

    if not os.path.exists(path) or not path.endswith(".txt"):
        path = create_default_text_file()
    try:
        raw_text = read_text_file(path)
        words = re.findall(r"\b[\w']+\b", raw_text.lower())
        words_occurrences = {word: words.count(word) for word in words}
        print("|             WORD             | OCCURRENCES |")
        print("="*46)
        for word, occurrences in words_occurrences.items():
            print(f"|{word_spaces(30, word)}|{word_spaces(13, str(occurrences))}|")
        print("="*46,f"\n Total: {len(words)} words, {len(words_occurrences)} unique words.")
    except Exception as e:
        print("Sorry! An error occurred while trying to read the file, you can try again or turn off your computer and never turn it on again.")
    
def read_text_file(path)->str:
    with open(path,"r",encoding="utf8") as file:
        return file.read()

def create_default_text_file()->str:
    path = "./sample_text.txt"
    nouns = ['cat', 'dog', 'tree', 'house', 'car']
    verbs = ['runs', 'jumps', 'sleeps', 'eats', 'drives']
    adjectives = ['big', 'small', 'happy', 'sad', 'beautiful']
    adverbs = ['quickly', 'slowly', 'loudly', 'quietly', 'happily']
    with open(path,"w") as file:
        for _ in range(20):
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            adjective = random.choice(adjectives)
            adverb = random.choice(adverbs)
            file.write(f"The {adjective} {noun} {verb} {adverb}.\n")
    return path


class BankAccount():
    """Bank account
    \nmethods: 
    \n-deposit
    \n-withdraw
    \n-get_balance
    """
    def __init__(self, balance:float = 0.0):
        self._balance = balance
    def deposit(self, amount:float|int)-> float:
        amount = abs(amount)
        if amount == 0:
            raise InvalidAmountError("The amount to deposit must be greater than 0")
        self._balance+= amount
        return self._balance
    def withdraw(self, amount:float|int)-> float:
        amount = abs(amount)
        if self._balance == 0:
            raise InsufficientFundsError("Withdrawal not available, your account balance is 0")
        if self._balance < amount:
            raise InsufficientFundsError("Insufficient funds")
        if amount <= 0:
            raise InvalidAmountError("The amount to withdraw must be greater than 0")
        self._balance -= amount
        return self._balance
    def get_balance(self)->float:
        return self._balance
    
class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass

class BankMenu():

    def __init__(self, account:BankAccount = BankAccount()) -> None:
        self.account = account
        self.main()

    def main(self):
        options = {
            1: self.deposit,
            2: self.withdraw,
            3: self.balance,
            4: lambda: "Thanks for using our bank"
        }
        selection = None
        while not selection:
            os.system("clear")
            print("**** Account Menu ****")
            print("     1- Deposit")
            print("     2- Withdraw")
            print("     3- Balance")
            print("     4- exit")
            selection = input_request("Write the number of your choice: ")
            os.system("clear")
            selection = options.get(selection, lambda:None)()
        print(selection)

    def deposit(self):
        print("**** Deposit ****\n")
        amount = input_request("Write the amount to deposit: ",float)
        try:
            new_balance = self.account.deposit(amount)
            print(f"successful deposit, your balance: ${new_balance}")
        except InvalidAmountError as e:
            print(e)
        input("press enter to continue...\n ")

    def withdraw(self):
        print("**** Withdraw ****\n")
        amount = input_request("Write the amount to withdraw: ",float)
        try:
            new_balance = self.account.withdraw(amount)
            print(f"successful withdrawal, your balance: ${new_balance}")
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(e)
        input("press enter to continue:\n ")

    def balance(self):
        print("**** Balance ****\n")
        print(f"Your account balance: {self.account.get_balance()}")
        input("Press enter to continue...")
