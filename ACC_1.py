def findTwoNonRepeatingNumbers(arr):
    unique_numbers = set()
    for num in arr:
        if num in unique_numbers:
            unique_numbers.remove(num)
        else:
            unique_numbers.add(num)
    result = list(unique_numbers)
    result.sort()
    return result

arr1 = [1, 2, 3, 2, 1, 4]  
result1 = findTwoNonRepeatingNumbers(arr1)
print(result1[0], result1[1])

arr2 = [2, 1, 3, 2]  
result2 = findTwoNonRepeatingNumbers(arr2)
print(result2[0], result2[1])
