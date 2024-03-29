def MergeSort(lists):
	if len(lists) <= 1:
		return lists
	num = len(lists)//2
	left = MergeSort(lists[:num])
	right = MergeSort(lists[num:])
	return Merge(left,right)
	
def Merge(left,right):
	l, r = 0, 0
	result = []
	while l<len(left) and r<len(right):
		if left[l] <=right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += list(left[l:])
	result += list(right[r:])
	return result
print MergeSort([1,2,3,4,5,6,7,90,21,23,45])
