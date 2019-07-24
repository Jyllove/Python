def bubblesort(array):
    for i in range(len(array)):
        for j in range(1,len(array)-i):
            if array[j-1]>array[j]:
                array[j-1],array[j] = array[j],array[j-1]
        


if __name__ == "__main__":
    array = [1,4,6,7,3,8,9,2,5,10]
    print("raw array is: ",end="")
    print(array)
    bubblesort(array)
    print("sorted array is: ",end="")
    print(array)
