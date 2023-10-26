# python implementation 
from typing import List

def get_max(arr: List[int]) -> int: 
	mx = arr[0] 
	for i in range(1, len(arr)): 
		if arr[i] > mx: 
			mx = arr[i] 
	return mx 

def count_sort(arr: List[int], exp: int): 
	output = [0] * len(arr) 
	count = [0] * 10

	# Store count of occurrences in count[] 
	for i in range(len(arr)): 
		count[(arr[i] // exp) % 10] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output[] 
	for i in range(1, 10): 
		count[i] += count[i - 1] 

	# Build the output array 
	for i in range(len(arr) - 1, -1, -1): 
		output[count[(arr[i] // exp) % 10] - 1] = arr[i] 
		count[(arr[i] // exp) % 10] -= 1

	# Copy the output array to arr[], so that arr[] now 
	# contains sorted numbers according to current digit 
	for i in range(len(arr)): 
		arr[i] = output[i] 


def parallel_count_sort(arr: List[int]): 
	m = get_max(arr) 

	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is 10 ^ i 
	# where i is current digit number 
	exp = 1
	while m // exp > 0: 
		for i in range(len(arr)): 
			count_sort(arr, exp) 
		exp *= 10

# Driver program to test above functions 
def main(): 
	arr = [170, 45, 75, 90, 802, 24, 2, 66] 
	print("Array before sorting:") 
	print(arr) 

	parallel_count_sort(arr) 

	print("Array after sorting:") 
	print(arr) 

if __name__ == "__main__": 
	main() 

# This code is contributed by ksam24000 
