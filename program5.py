# Sum of number digits in List
# Approach 1
'''def sum_of_number_digits(input_list):
    updated_list = []
    for number in input_list:
        sum = 0
        for digit in str(number):
            sum += int(digit)
        updated_list.append(sum)
    return updated_list'''

# Approach 2
from functools import reduce

def sum_of_number_digits(input_list):
    updated_list = [reduce(lambda x, y : int(x) + int(y), list(str(number))) for number in input_list]
    return updated_list

def main():
    input_list = [12, 67, 98, 34]
    print("Initial list : {}" .format(input_list))
    result = sum_of_number_digits(input_list)
    print("Updated list : {}".format(result))

if __name__ == '__main__':
    main()
