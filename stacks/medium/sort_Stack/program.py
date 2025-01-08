def sortStack(array: list) -> list:
    if len(array) <= 1:
        return array

    cur_value = array.pop()

    sortStack(array)

    insertInSortedOrder(array, cur_value)

    return array


def insertInSortedOrder(stack: list, value: int) -> None:
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    bigger_value = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(bigger_value)