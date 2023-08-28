
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