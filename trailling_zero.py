nums = [1,2,3,4,5]

#You are given an array of positive integers nums.

#You have to check if it is possible to select two or more elements in the array such that the bitwise OR of 
#the selected elements has at least one trailing zero in its binary representation.

#For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas 
#the binary representation of 4, which is "100", has two trailing zeros.

#Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.


def trailingzeros(lst):
	count = 0
	for n in lst:
		if n%2 == 0:
			count += 1
		if count == 2:
			return True
	return False

print(trailingzeros(nums))


#Solution: The only way we can have trailing zeros at the right is if both the numbers have 0 at the rightmost bit

#It only happens with both numbers being pair