# In processing raw text, it’s quite often necessary to clean and normalize the text before doing anything else. 
#If you want to find the frequency of words in text, for example, you can make the job easier if, before you start counting, 
#you make sure that everything is lowercase (or uppercase, if you prefer) and that all punctuation has been removed. 
#You can also make things easier by breaking the text into a series of words. In this lab,the task is to read 
#the first part of the first chapter of Moby Dick (found in the book's source code), make sure that everything is one case,
#remove all punctuation, and write the words one per line to a second file

punct_table = str.maketrans("!.,:;-?'", "        ")

with open('moby_01.txt', 'r') as infile, open('moby_clean_01.txt', "w") as outfile:
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
            cleaned_words = "\n".join(words)
            # Write all words for line
            outfile.write(cleaned_words+"\n")
        
    infile.close()
    outfile.close()
    