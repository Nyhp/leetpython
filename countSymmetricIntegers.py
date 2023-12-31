#You are given two positive integers low and high.

#An integer x consisting of 2 * n digits is symmetric if 
#the sum of the first n digits of x is equal to the sum of the 
#last n digits of x. Numbers with an odd number of digits are never symmetric.

#Return the number of symmetric integers in the range [low, high].

def countSymmetricIntegers(low: int, high: int) -> int:
    count = 0
    for i in range(low, high + 1):
        summ = 0
        num = str(i)
        length = len(str(i))
        if length % 2 == 0:
            for j in range(length//2):
                summ += (int(num[j]) - int(num[length - j - 1]))
            if (summ == 0):
                count += 1
    return count


print(countSymmetricIntegers(1200,1230))