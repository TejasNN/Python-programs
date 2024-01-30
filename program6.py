# Program to print duplicates from a list of integers

def remove_duplicates(input_list):
    new_dict, new_list = {}, []

    for num in input_list:
        if not num in new_dict:
            new_dict[num] = 1
        else:
            new_dict[num] += 1
    
    for key, value in new_dict.items():
        if value > 1:
            new_list.append(key)
    
    return new_list

def main():
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    print(remove_duplicates(input_list))

if __name__ == '__main__':
    main()