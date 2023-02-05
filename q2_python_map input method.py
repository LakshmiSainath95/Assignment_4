
#Python program to triple all numbers of a given list of integers. Use Python map.

nums = []

# number of elements as input
n = int(input("Enter number of elements : "))  # here i given 4 as size of list and then entered 4,5,2,9 as input elements

# iterating till the range
for i in range(0, n):
	ele = int(input())

	nums.append(ele) # adding the element
	
print(nums)

# sample_lst = (1, 2, 3, 4, 5, 6, 7) 

print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of given list numbers:")
print(list(result))