#Find the Minimum Possible Sum of a Beautiful Array
#Given positive integers 'n' and 'target'
#An array is beautiful if it meets the following conditions:
# - it's length is 'n'
# - it's elements are pairwise distinct
# - There doesn't exist two distinct elements such that their sum are equal to 'target'
#Return the minimum possible sum that a beautiful array could have.

def minimumPossibleSum(n, target) -> int:
    if n == 1:
        return 1
    else:
        array = []
        counter = 1
        while(len(array) < n):
            if((target - counter) not in array):
                array.append(counter)
            counter += 1
        print(array)
        return sum(array)   

print(minimumPossibleSum(3,3))