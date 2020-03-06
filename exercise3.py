def merge_intervals(interval_1, interval_2):
    threshold_left = int(interval_1[0])
    threshold_right = int(interval_1[1])
    if threshold_left in range(*interval_2) and threshold_right not in range(*interval_2):
        interval_2[1] = threshold_right
        return interval_2
    elif threshold_right in range(*interval_2) and threshold_left not in range(*interval_2):
        interval_2[0] = threshold_left
        return interval_2
    elif threshold_right in range(*interval_2) and threshold_left in range(*interval_2):
        return interval_2
    else:
        return None


current_intervals = []
while True:
    new_interval = [int(i) for i in input().split(',')]
    local_intervals = list(current_intervals)
    for interval in local_intervals:
        temp_interval = merge_intervals(new_interval, interval)
        if temp_interval:
            current_intervals.pop(current_intervals.index(interval))
            new_interval = temp_interval
        else:
            continue
    current_intervals.append(new_interval)
    print(sum([(int(i[1])-int(i[0])) for i in current_intervals]))