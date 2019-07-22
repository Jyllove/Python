def quick_sort(array,left,right):
    if right>left:
        p = partitions(array,left,right)
        quick_sort(array,left,p)
        quick_sort(array,p+1,right)


def partitions(array,left,right):
    mid = array[right]
    i = left-1
    for j in range(left,right):
        if array[j]<=mid:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[right] = array[right],array[i+1]
    
    return i


if __name__ == "__main__":
    array = [1,3,5,7,9,2,11,13,4,6,8,10,12,15,17,19,14,16,18,20]
    print("raw array is: ",end="")
    print(array)
    quick_sort(array,0,len(array)-1)
    print("sorted array is: ",end="")
    print(array)
