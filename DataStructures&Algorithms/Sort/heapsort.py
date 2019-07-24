def heap(array,start,end):
    root = start
    child = root*2+1
    while child<=end:
        if child+1<=end and array[child]<array[child+1]:
            child += 1
        if array[root]<array[child]:
            array[root],array[child] = array[child],array[root]
            root = child
            child = root*2+1
        else:
            break

def heap_sort(array):
    first = len(array)//2-1
    for start in range(first,-1,-1):
        heap(array,start,len(array)-1)
    for end in range(len(array)-1,0,-1):
        array[0],array[end] = array[end],array[0]
        heap(array,0,end-1)


if __name__ == "__main__":
    array = [1,4,6,7,3,8,9,2,5,10]
    print("raw array is: ",end="")
    print(array)
    heap_sort(array)
    print("sorted array is: ",end="")
    print(array)
