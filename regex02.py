import re

message = 'Call me 415-555-1011 tomorrow, or at 415-666-9999'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
mo = phoneNumRegex.findall(message)
print(mo)
print()


message = 'Call me (415) 555-1011 tomorrow, or at 415-666-9999'
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
mo = phoneNumRegex.findall(message)
print(mo)
print()
print()


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile and Batman lost a wheel')
print(mo.group())
print(mo.group(1))

mo = batRegex.findall('Batmobile and Batman lost a wheel')
print(mo)


"""
To recap:

- Groups are created in regex strings with parentheses.
- The first set of parentheses in group 1, the second is 2, and so on.
- Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
- Use \( and \) to match literal parentheses in the regex string.
- The | pipe match one of many possibles groups.
"""
