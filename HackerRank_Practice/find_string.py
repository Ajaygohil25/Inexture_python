# n this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# note: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Constraints
# Each character in the string is an ascii character.
# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string

str1 = input("Input string : ")
str2 = input("Input substring : ")

count=0
for i in range(len(str1)):
    sub_str = str1[i: i+3]
    if sub_str==str2:
        count+=1
print(count)
