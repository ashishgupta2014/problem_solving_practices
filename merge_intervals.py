def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals = sorted(intervals)
    output = [intervals[0]]
    for i in range(1, len(intervals)):
        last = output[-1]
        start = intervals[i][0]
        end = intervals[i][1]
        if last[1] >= start and end >= last[1]:
            output[len(output)-1][1] = end
        elif last[1] < start and last[1] < end:
            output.append(intervals[i])
    return output
print(merge([[1,4],[4,5]]))
