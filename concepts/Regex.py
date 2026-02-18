import re

s = "GeeksforGeeks: A computer science portal for geeks"
match= re.search(r"portal",s)
print(f"Matching result:{match}")

print('Start Index:', match.start())
print('End Index:', match.end())

## search() method finds the first occurence of the pattern in a given string
## returns match object if match is found else returns None


## to find count of all the occurences of "#"  in the given string
text = "Be #yourself; everyone else is already taken."
count = len(re.findall("#", text))
print(count)  # Output: 1

