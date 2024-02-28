# find out if the given two strings are anagrams or not?

def chkAnagram(input1: str, input2: str) -> bool:
    if (len(input1) != len(input2)):
        return False
    
    # Create a empty dictionary
    counts = {}

    # loop through both the strings and check if the char is in dictionary
    for c1, c2 in zip(input1, input2):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1

        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1

    # traverse through counts dict
    for count in counts.values():
        if count != 0:
            return False    
    return True

def main():
    input1 = "listen"
    input2 = "silent"

    if chkAnagram(input1, input2):
        print(f"{input1} and {input2} are anagrams")
    else:
        print(f"{input1} and {input2} are not anagrams")

if __name__== '__main__':
    main()