def interweavingStrings(one: str, two: str, three: str) -> bool:

    if one == '' and two == '' and three == '':
        return True

    if three == '':
        return False
    else:
        letter3 = three[0]

    if one != '':
        letter1 = one[0]

        if letter3 == letter1:
            result = interweavingStrings(one[1:], two, three[1:])

            if result:
                return True

    if two != '':
        letter2 = two[0]

        if letter3 == letter2:

            result = interweavingStrings(one, two[1:], three[1:])

            if result:
                return True

    return False