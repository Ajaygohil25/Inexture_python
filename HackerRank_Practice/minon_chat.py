def check_vowel(char):
    return char in 'aeiouAEIOU'

def minion_game(string):
    score_kevin = 0
    score_stuart = 0
    length = len(string)
    
    for i in range(length):
        char = string[i]
        # Calculate scores based on the starting position of substrings
        if check_vowel(char):
            score_kevin += length - i  # All substrings starting from this index are Kevin's
        else:
            score_stuart += length - i  # All substrings starting from this index are Stuart's

    if score_stuart > score_kevin:
        print(f"Stuart {score_stuart}")
    elif score_kevin > score_stuart:
        print(f"Kevin {score_kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
