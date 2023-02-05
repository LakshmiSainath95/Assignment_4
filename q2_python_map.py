
#Python program to triple all numbers of a given list of integers. Use Python map.

sample_lst = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", sample_lst)
result = map(lambda x: x + x + x, sample_lst) 
print("\nTriple of given list numbers:")
print(list(result))