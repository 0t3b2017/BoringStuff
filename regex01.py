"""
Phone number (US) 415-555-0000
Phone number (BR) +55-11-5612-0000
M Phone number (BR) +55 11 95612 0000
"""


"""
# Without RE

def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing the last 4 digits
    return True

# print(isPhoneNumber('443-555-1234'))
# print(isPhoneNumber('hello'))

message = 'Call me 415-555-1011 tomorrow, or at 415-666-9999'
foundNumber = False

# Passa Loop por toda sequencia de 12 de caracteres da string pelo index
# print(len(message))
for i in range(len(message)):
    # print('.')
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: {}'.format(chunk))
        foundNumber = True

if not foundNumber:
    print("Could not find any phone numbers.")

"""

# With RE

import re

message = 'Call me 415-555-1011 tomorrow, or at 415-666-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(type(phoneNumRegex))
# print(phoneNumRegex)

# search, returns <class '_sre.SRE_Match'> object with the fisrt regex match
mo = phoneNumRegex.search(message)
print(type(mo))
print(mo.group())

# findall, returns a list with all regex found
mo = phoneNumRegex.findall(message)
print(type(mo))
print(mo)

"""
To recap:

- Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without 
regular expressions is a huge pain.
- Regex stringhs often use \ backslashes (like \d), so they are often raw strings: r'\d'
- Import the re module first
- Call the re.compile() function to create a regex object.
- Call the regex object's search() method to create a match object.
- Call the match object's group() method to get the matched string.
- \d is the regex for a numeric digit character.
"""
