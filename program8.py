# Length of last word

def lengthOfLastWord(s : str) -> int:
    totalLength = len(s)
    index = totalLength - 1

    while s[index] == ' ': index -= 1
    
    letter_count = 0
    for i in range(index, 0, -1):
        if s[i] != ' ':
            letter_count += 1
        else:
            break

    return letter_count

def main():
    input_string = 'This the end of line '
    print(lengthOfLastWord(input_string))

if __name__ == '__main__':
    main()