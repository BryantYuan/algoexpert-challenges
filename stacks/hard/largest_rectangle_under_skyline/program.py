def largestRectangleUnderSkyline(buildings):
    stack = []
    largest = 0
    cur_index = 0

    for building in buildings:

        while stack:

            last_index = stack[-1]
            last_value = buildings[last_index]

            if last_value > building:

                stack.pop()

                margins = cur_index - last_index if not stack else cur_index - (stack[-1] + 1)

                new_area = margins * last_value

                if new_area > largest:
                    largest = new_area

            else:
                break

        stack.append(cur_index)

        cur_index += 1


    while stack:

        index = stack.pop()
        value = buildings[index]

        margins = len(buildings) - index if not stack else len(buildings) - (stack[-1] + 1)

        area = margins * value

        if area > largest:
            largest = area

    return largest


print(largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]))