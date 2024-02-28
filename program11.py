#Find the number of occurrences of a character in a String

def checkCharacter(string: str, character: str) -> int:
    count = 0

    for ch in string:
        if ch == character:
            count += 1
    return count

print(checkCharacter("Hello", 'l'))