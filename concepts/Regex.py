import re

s = "GeeksforGeeks: A computer science portal for geeks"
match= re.search(r"portal",s)
print(f"Matching result:{match}")

print('Start Index:', match.start())
print('End Index:', match.end())