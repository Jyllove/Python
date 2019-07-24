def shell_sort(array):
    length = len(array)
    while length>=1:
        length = length//2
        for i in range(length):
            for j in range(1,len(range(i,len(array),length))):
                temp = array[i+j*length]
                k=j
                while temp<array[i+(k-1)*length] and k>=1:
                    array[i+k*length] = array[i+(k-1)*length]
                    k -= 1
                array[i+k*length] = temp
                

if __name__ == "__main__":
    array = [1,4,6,7,3,8,9,2,5,10]
    print("raw array:",end="")
    print(array)
    shell_sort(array)
    print("ordered array:",end="")
    print(array)
