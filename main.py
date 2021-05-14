def two_sum(arr, target):  # O (n) tc && sc
    sums = {}
    for i in arr:
        poss = target - i
        if poss in sums:
            return [i, poss]
        sums[i] = ""
    return []


# [1, 3, 5], 8
# [3, 5]

def dumb_two_sum(arr, target):  # O(n^2) tc
    for i in arr:
        for j in arr:
            if i + j == target:
                return [i + j]
    return []

