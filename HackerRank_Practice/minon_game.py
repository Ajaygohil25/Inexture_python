# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# Sample Input
# BANANA
# Sample Output
# Stuart 12

# Stuarat --> consonent at begining , Kevin -> vowel at beginning
# approach: first go through all string, create two dictonary Stuarat and kevin ,
#  pass all substring based on it's first character wheter it's consonant or vowel

#  BANANA

def check_vowels(word):
    vowel ={'a','e','i','o','u','A','E','I','O','U'}
    if word in vowel:
        return True
    return False

def minion_game(string):
    # your code goes here
    Stuarat={}
    Kevin={}

    for i in string:
        if check_vowels(i):
            if i in Kevin.keys():
                Kevin[i]+=1
            else:     
                Kevin[i]=1
            # print("Stuarat", Stuarat)
        else:
            if i in Stuarat.keys():
                 Stuarat[i]+=1
            else:     
                Stuarat[i]=1
            # print("kevin", Kevin) 
    for i in range(0,len(string)):
        for j in range(i+1, len(string)):
            subStr = string[i:j+1]
            # print("substr:", subStr)
            # check all the substring's first characetr for the vowels and consonent 
            if check_vowels(subStr[0]):
                if subStr in Kevin.keys():
                    Kevin[subStr]+=1
                else:     
                    Kevin[subStr]=1
            else:
                if subStr in Stuarat.keys():
                    Stuarat[subStr]+=1
                else:     
                    Stuarat[subStr]=1
    Score_S=0
    for i in Stuarat.values():
        Score_S+=i
    Score_k=0
    for k in Kevin.values():
        Score_k+=k
    if Score_S >Score_k:
        print("Stuart ",Score_S)
    elif Score_k> Score_S:
        print("Kevin ",Score_k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)



# banana  ==> ba an na an na ==> ban, ana, 

# smart work , optimal solution:
def check_vowel(word):
    vowel ={'a','e','i','o','u','A','E','I','O','U'}
    if word in vowel:
        return True
    return False

def minion_game(string):
    score_kevin = 0
    score_stuart = 0
    length = len(string)
    
    for i in range(length):
        char = string[i]
        # Calculate scores based on the starting position of substrings
        if check_vowel(char):
            score_kevin += length - i 
        else:
            score_stuart += length - i 

    if score_stuart > score_kevin:
        print(f"Stuart {score_stuart}")
    elif score_kevin > score_stuart:
        print(f"Kevin {score_kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
