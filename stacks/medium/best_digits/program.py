def bestDigits(number: str, numDigits: int) -> str:
    index = 0
    stack = []
    length = len(number)

    while index < length:
        cur_value = int(number[index]) # Takes current value

        if stack: # Checks for empty stack

            # Will keep popping if cur_value is larger than next value in stack, and we still have digits to delete
            while cur_value > int(stack[-1]) and numDigits > 0: # Turns value in stack to int because the values are str

                stack.pop() # Remove the smaller digit
                numDigits -= 1 # We have now removed one of the digits, hence must subtract it from numDigits

                if not stack: # If stack is empty, leave
                    break



        stack.append(str(cur_value)) # We need str because the '.join' func we use later can only have List[str].

        index += 1

    if numDigits > 0: # Checks if we have anymore numbers to delete

        for i in range(numDigits):
            stack.pop() # All the smallest numbers are at the end. Therefore, we simply pop them

    return ''.join(stack) # Turns the stack into str (The output must be str). This func only supports list of str