import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'start', re.I)

# matches = pattern.search(sentence)

# print(matches)

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})', '26-08-2020')
print(grp)

## Print the entire match using group() function 
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group())

## Return a tuple of matching groups
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.groups())

## Retrieve a single group
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group(0))
print(grp.group(1))
print(grp.group(2))
print(grp.group(3))