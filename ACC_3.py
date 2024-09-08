def getMaxToys(prices, money):
    max_toys = 0
    current_sum = 0
    left = 0

    for right in range(len(prices)):
        current_sum += prices[right]

        # If current_sum exceeds money, move the left pointer to reduce the sum
        while current_sum > money:
            current_sum -= prices[left]
            left += 1

        # Update max_toys if we found a longer subarray
        max_toys = max(max_toys, right - left + 1)

    return max_toys

# Example usage:
prices = [1, 4, 5, 3, 2, 1, 6]
money = 6
print(getMaxToys(prices, money))  # Output: 3
