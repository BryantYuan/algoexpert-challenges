def mergeOverlappingIntervals(intervals):
    intervals.sort()
    current_index = 0

    while current_index < len(intervals) - 1:
        cur_interval = intervals[current_index]
        next_interval = intervals[current_index + 1]

        if cur_interval[-1] >= next_interval[0]:
            cur_interval[-1] = max(cur_interval[-1], next_interval[-1])
            del intervals[current_index + 1]
        else:
            current_index += 1

    return intervals
111111