# Rotate array for k = 3

def arrayReverse(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    
def rightrotate(arr, rotate):
    if rotate == 0:
        return
    array_length = len(arr)
    index = array_length - rotate
    rotate = rotate % array_length

    arrayReverse(arr, index, array_length-1)
    arrayReverse(arr, 0, index-1)
    arrayReverse(arr, 0, array_length-1)

if __name__ == '__main__':
    arr = [7,3,2,6,1,8,5]
    k = 3
    rightrotate(arr,k)
    print(arr)