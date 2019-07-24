import math
 
def radix_sort(array):
    radix = 10
    K = 0
    m = max(array)
    while m!=0:
        K += 1
        m /= 10
    bucket = [[] for i in range(radix)]
    for i in range(1,K+1):    
        for item in array:
            bucket[item%(radix**i)//(radix**(i-1))].append(item)
        del array[:]
        for buck in bucket:
            array.extend(buck)
        bucket = [[] for i in range(radix)]
            

if __name__ == "__main__":
    array = [1,4,6,7,3,8,9,2,5,10]
    radix_sort(array)
    print(array)
