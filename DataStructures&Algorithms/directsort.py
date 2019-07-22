def direct_insert_sort(array):
  for i in range(1,len(array)):
    temp = array[i]
    j = i-1
    while j>=0 and temp<array[j]:
      array[j+1]=array[j]
      j = j-1
    array[j+1] = temp
        

if __name__ == "__main__":
    array = [1,3,5,7,9,2,11,13,4,6,8,10,12,15,17,19,14,16,18,20]
    print("raw array is: ",end="")
    print(array)
    direct_insert_sort(array)
    print("sorted array is: ",end="")
    print(array)
