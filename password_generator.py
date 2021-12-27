from string import ascii_letters, digits, punctuation
from random import randint

char_type_mapping = {
    0: ascii_letters,
    1: digits,
    2: punctuation
}
number_of_char_types = len(char_type_mapping) 

password = ""

counter = 0
while counter < 64:
    char_type = char_type_mapping[randint(0, number_of_char_types - 1)]
    password += char_type[randint(0, len(char_type) - 1)]

    counter += 1

print(password)