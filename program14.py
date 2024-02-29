# Linear search

def LinearSearch(list1: list, value: int) -> bool:
    bFlag = False
    for num in list1:
        if (num == value):
            bFlag = True
            break
    return bFlag

def main():
    input_list = []
    num = int(input("Enter number of elements: "))
    for i in range(num):
        element = int(input())
        input_list.append(element)
    value = int(input("Enter a value to seach: "))
    bResult = LinearSearch(input_list, value)
    if(bResult == True):
        print(f"{value} found")
    else:
        print(f"{value} not found")

if __name__ == '__main__':
    main()