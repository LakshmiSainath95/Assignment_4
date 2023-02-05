# Python program to square the elements of a list using map() function.

def square_num(n):
  return n * n

# creating an empty list
nums = []

# number of elements as input
n = int(input("Enter number of elements : "))  # here i given 4 as size of list and then entered 4,5,2,9 as input elements

# iterating till the range
for i in range(0, n):
	ele = int(input())

	nums.append(ele) # adding the element
	
print(nums)

print("Original List: ",nums)
result = map(square_num, nums)
print("Squares of the list using map(): ")
print(list(result))
