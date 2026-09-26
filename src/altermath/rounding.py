def floor(*nums):
    if not nums:
        return None
    r = []
    for n in nums:
        i = int(n)
        if n < i:
            r.append(i - 1)
        else:
            r.append(i)
    return r[0] if len(r) == 1 else r


def ceil(*nums):
    if not nums:
        return None
    r = []
    for n in nums:
        i = int(n)
        if n > i:
            r.append(i + 1)
        else:
            r.append(i)
    return r[0] if len(r) == 1 else r


def trunc(*nums):
    if not nums:
        return None
    r = []
    for n in nums:
        r.append(int(n))
    return r[0] if len(r) == 1 else r
