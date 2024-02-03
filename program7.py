# Extract elements with Frequency greater than K

def Numbers_frequency(lst, value):
    unique_ele = []
    freq_num = {}
    output_list = []
    for num in lst:
        if not num in unique_ele:
            unique_ele.append(num)
            freq_num[num] = 1
        else:
            freq_num[num] += 1

        if freq_num[num] == value + 1:
            output_list.append(num)
            
    return output_list

def main():
    input_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8, 4]
    k = 2
    print(Numbers_frequency(input_list, k))

if __name__ == '__main__':
    main()