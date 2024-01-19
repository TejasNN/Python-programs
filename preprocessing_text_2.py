# In processing raw text, it’s quite often necessary to clean and normalize the text before doing anything else. 
#If you want to find the frequency of words in text, for example, you can make the job easier if, before you start counting, 
#you make sure that everything is lowercase (or uppercase, if you prefer) and that all punctuation has been removed. 
#You can also make things easier by breaking the text into a series of words. In this lab,the task is to read 
#the first part of the first chapter of Moby Dick (found in the book's source code), make sure that everything is one case,
#remove all punctuation, and use a dictionary to count the number of imes each word occurs, and then report the most common and least common words.

punct_table = str.maketrans("!.,:;-?'", "        ")
cleaned_words = {}

with open('moby_01.txt', 'r') as infile:
    for line in infile:
        # make all one case
        cleaned_line = line.lower()

        # remove punctuations
        cleaned_line = cleaned_line.translate(punct_table)

        # split into words
        words = cleaned_line.split()

        # Checking for paragraph
        if words == []:
            continue
        else:
            #cleaned_words = "\n".join(words)
            for word in words:
                cleaned_words[word] = cleaned_words.get(word, 0) + 1        
    
    word_list = list(cleaned_words.items())
    word_list.sort(key=lambda x:x[1])

    print("Most common words :")
    for word in reversed(word_list[-5:]):
        print(word)
    print("Least common words :")
    for word in word_list[:5]:
        print(word)
    infile.close()
    