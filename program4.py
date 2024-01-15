# Reverse the list

input_list = [4, 6, 3, 8, 5]
print("Initial list : " % input_list)
#using two pointer approach

start = 0
end = len(input_list) - 1

while start < end:
    temp = input_list[start]
    input_list[start] = input_list[end]
    input_list[end] = temp
    start += 1
    end -= 1

print(input_list)
