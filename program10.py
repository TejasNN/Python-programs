# how to determine if string is palindrome

def chkPalindrome(data):
    original_string = data

    modified_string = data[::-1]

    return original_string == modified_string
string1 = "aba"
print(chkPalindrome(string1))