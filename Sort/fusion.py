from visualisationTri import visualisation

def merge(L, left, right):
    if left>= right:
        return

    mid = (left+right)//2
    merge(L, left, mid)
    merge(L, mid+1, right)

    fusion(L, left, right, mid)

def fusion(L, left, right, mid):
    leftCopy = L[left : mid+1]
    rightCopy = L[mid+1 : right+1]

    lCounter, rCounter = 0, 0
    sortedCounter = left

    while lCounter<len(leftCopy) and rCounter<len(rightCopy):
        if leftCopy