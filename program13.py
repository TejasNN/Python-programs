# How do you calculate the number of vowels and consonants in a String

def calculate_vowel_consonants(data: str) -> None:
    # Take vowel set
    vowel = set("aeiouAEIOU")

    # Take two counters one for vowel count and another for consonants
    vowel_count = consonant_count = 0

    for ch in data:
        if ch in vowel:
            vowel_count += 1
        else:
            consonant_count += 1
            
    print("Vowels count is : {}".format(vowel_count))
    print("Consonants count is : {}".format(consonant_count))

def main():
    input = "GeeksForGeeks"
    calculate_vowel_consonants(input)

if __name__ == '__main__':
    main()
    