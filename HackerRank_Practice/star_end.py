# start() & end()
# These expressions return the indices of the start and end of the substring matched by the group.

# Code

# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0
# Task
# You are given a string .
# Your task is to find the indices of the start and end of string  in .

# Input Format

# The first line contains the string .
# The second line contains the string .

# Constraints



# Output Format

# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).

# Sample Input

# aaadaa
# aa
# Sample Output

# (0, 1)  
# (1, 2)
# (4, 5)

import re

string = input()
substr =  input()

pattern=f"(?=({substr}))"
matches  = re.finditer(pattern, string)
indices=[]
for match in matches :
    indices.append((match.start(), match.start()+ len(substr)-1))

for i  in indices:
    print(i)    






