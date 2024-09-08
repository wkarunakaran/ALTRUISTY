def findSteppingNumbers(n, m):
    def isStepping(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if abs(int(num_str[i]) - int(num_str[i - 1])) != 1:
                return False
        return True
    result = []
    for i in range(max(0, n), m + 1):
        if isStepping(i):
            result.append(i)
    return result
n, m = map(int, input().split())
stepping_numbers = findSteppingNumbers(n, m)
print(*stepping_numbers)
