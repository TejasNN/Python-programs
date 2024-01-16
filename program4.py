# Reverse the list
#using two pointer approach

def list_reverse(input_list):
    start = 0
    end = len(input_list) - 1

    while start < end:
        temp = input_list[start]
        input_list[start] = input_list[end]
        input_list[end] = temp
        start += 1
        end -= 1

def main():
    input_list = [4, 6, 3, 8, 5]
    print("Initial list : {}" .format(input_list))
    list_reverse(input_list)
    print("reversed list : {}" .format(input_list))

if __name__=='__main__':
    main() 
