def minimizeTicketCost(ticket: str, k: int) -> str:
    stack = []
    for digit in ticket:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')  
    return result if result else "0"
ticket = "203"
k = 2
print(minimizeTicketCost(ticket, k)) 
