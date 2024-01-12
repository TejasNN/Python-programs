# Python program to interchange first and last elements in a list

# Approach 1
def swap_first_last_element_approach_1(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

# Approach 2
def swap_first_last_element_approach_2(new_list):
    start, *middle, end = new_list
    new_list = [end, *middle, start]
    return new_list

input_list = [12, 35, 9, 56, 24]

print(swap_first_last_element_approach_1(input_list))
print(swap_first_last_element_approach_2(input_list))