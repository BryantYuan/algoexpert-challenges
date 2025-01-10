def oneEdit(stingOne: str, stingTwo: str) -> bool:

    length1 = len(stingOne)
    length2 = len(stingTwo)

    if abs(length1 - length2) > 1:
        return False


    index1 = 0
    index2 = 0
    diff_count = 0

    smallerLength = min(length1, length2)


    while index1 < length1 and index2 < length2:

        if stingOne[index1] != stingTwo[index2]:
            diff_count += 1

            if length1 == length2:

                index1 += 1
                index2 += 1

                continue

            if smallerLength == length1:
                index2 += 1

            else:
                index1 += 1

        else:

            index1 += 1
            index2 += 1

        if diff_count > 1:
            return False

    if diff_count > 1:
        return False

    return True