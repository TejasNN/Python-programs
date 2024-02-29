# Bi-directional search

def biDirectionalSearch(input:list, value:int) -> bool:
    bFlag = False
    iStart = 0
    iEnd = len(input)-1

    while(iStart <= iEnd):
        if(input[iStart] == value or input[iEnd] == value):
            bFlag = True
            break
        iStart += 1
        iEnd -= 1
    return bFlag


def main():
    input_list = []
    num = int(input("Enter number of elements: "))
    for i in range(num):
        element = int(input())
        input_list.append(element)
    value = int(input("Enter a value to seach: "))
    bResult = biDirectionalSearch(input_list, value)
    if(bResult == True):
        print(f"{value} found")
    else:
        print(f"{value} not found")

if __name__ == '__main__':
    main()