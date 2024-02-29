# Binary search

def binarySearch(input:list, value:int) -> bool:
    # Make sure that the list is sorted
    # Then apply the below logic
    bFlag = False
    iStart = iMid = 0
    iEnd = len(input)-1
    
    while(iStart <= iEnd):
        iMid = iStart + int((iEnd - iStart) / 2)
        if(input[iMid] == value or input[iStart] == value or input[iEnd] == value):
            bFlag = True
            break
        elif (input[iMid] < value):
            iStart = iMid + 1
        elif (input[iMid] > value):
            iEnd = iMid - 1
    return bFlag

def main():
    input_list = []
    num = int(input("Enter number of elements: "))
    for i in range(num):
        element = int(input())
        input_list.append(element)
    value = int(input("Enter a value to seach: "))
    bResult = binarySearch(input_list, value)
    if(bResult == True):
        print(f"{value} found")
    else:
        print(f"{value} not found")

if __name__ == '__main__':
    main()