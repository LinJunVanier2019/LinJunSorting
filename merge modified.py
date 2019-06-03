def mergesort(ilist, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(ilist, start, mid)
    yield from mergesort(ilist, mid + 1, end)
    yield from merge(ilist, start, mid, end)
    yield ilist

def merge(ilist, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if ilist[leftIdx] < ilist[rightIdx]:
            merged.append(ilist[leftIdx])
            leftIdx += 1
        else:
            merged.append(ilist[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(ilist[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(ilist[rightIdx])
        rightIdx += 1

    for i, sorted_num in enumerate(merged):
        ilist[start + i] = sorted_num
        yield ilist



