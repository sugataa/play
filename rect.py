import math
def make_rect(area):
    mid = int(math.sqrt(area))

    while area%mid is not 0:
        mid -= 1

    return [area/mid, mid]

# print(make_rect(20))

def overlap(l1, r1, l2, r2):
    # r2.y > l1.y or r1.y > l2.y
    if (l1[1] > r2[1]) and (r1[1] < l2[1]):
        return False
    # r1.x < l2.x or l1.x > r2.x
    if (r1[0] < l2[0]) or (l1[0] > r2[0]):
        return False
    return True
