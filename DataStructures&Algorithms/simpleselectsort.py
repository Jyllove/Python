def simple_select_sort(raw_array):
    ordered_array = []
    for i in range(len(raw_array)):
        minimum = raw_array[0]
        for j in range(1,len(raw_array)):
            if minimum > raw_array[j]:
                minimum = raw_array[j]
        raw_array.remove(minimum)
        ordered_array.append(minimum)
    return ordered_array
        


if __name__ == "__main__":
    raw_array = [1,4,6,7,3,8,9,2,5,10]
    print("raw array:",end="")
    print(raw_array)
    ordered_array = simple_select_sort(raw_array)
    print("ordered array:",end="")
    print(ordered_array)
