import re
from math import ceil
def input_request(message:str, type:type = int)->float|int|list:
    """Requests by console a number or numbers
    
    Keyword arguments:
    message: str -- the request message to show by console
    type: type -- the type wanted to be returned from the input 
    Return: float|int|list -- depending of argument type
    """
    numbers = None
    find_numbers = lambda input: re.findall('-?\d+(?:\.\d+)?', input)
    if type == list:
        while not numbers:
            numbers = find_numbers(input(message))
        return([float(num) if "." in num else int(num) for num in numbers])
    else:
        while not numbers:
            numbers = find_numbers(input(message))
        number = float(numbers[0])
        return number if type==float else int(number)

from enum import Enum


class Alignment(Enum):
    """Types of alignment."""
    CENTER = "c"
    LEFT = "l"
    RIGHT = "r"
    
def word_spaces(total_len:int, word:str, align:Alignment = Alignment.CENTER)-> str:
    """Fill with spaces to the left and/or right of a word to complete the desired length
    e.g. add_spaces_to_word(10,'hello') -> '  hello   '. added 2 spaces to the left and 3 spaces yo the right
    \nKeyword arguments:
    total_len: int -- desired length
    word: str -- the desired word to add spaces
    align: Alignment -- type of alignment, Center by default
    Return: the word aligned with spaces
    """
    word_len = len(word)
    total_spaces = total_len - word_len
    
    n_left = ceil(total_spaces/2) if align == Alignment.CENTER else 0 if align == Alignment.LEFT else total_spaces
    n_right = 0 if total_spaces==0 or align == Alignment.RIGHT else total_spaces - n_left
    return " "*n_left+word+" "*n_right