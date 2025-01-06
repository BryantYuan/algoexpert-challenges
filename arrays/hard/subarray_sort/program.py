def subarraySort(array):
    prev_num = -float('inf')
    subarray_start = -1
    subarray_end = -1

    for i in range(0, len(array)):
        cur_num = array[i]

        if cur_num >= prev_num:
            prev_num = cur_num
            continue
        else:
            subarray_end = i
            if subarray_start == -1:
                subarray_start = findSubarrayStart(array, i - 1, cur_num)
            else:
                new = findSubarrayStart(array, subarray_start, cur_num)
                if new < subarray_start:
                    subarray_start = new

    return [subarray_start, subarray_end]


def findSubarrayStart(array, prev_index, cur_num):
    prev_num = array[prev_index]

    while cur_num < prev_num:
        prev_index -= 1
        prev_num = array[prev_index]
        if prev_index < 0:
            return 0

    return prev_index + 1