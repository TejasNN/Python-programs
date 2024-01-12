# Count occurences of words in a file

#1. First ask user to input the filename
#2. open the file, read it and store it's words in a list.
#3. Count the number of occurences of those words in a dict.

def words_occur():
    file_name = input("Enter the name of the file: ")
    # Opening the file
    f = open("emptyFile.txt", 'r')
    word_list = f.read().split()
    f.close()
    occurs_dict = {}

    for word in word_list:
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    print("File %s has %d words (%d are unique)"
           % (file_name, len(word_list), len(occurs_dict)))
    print(occurs_dict)


if __name__ == '__main__':
    words_occur()