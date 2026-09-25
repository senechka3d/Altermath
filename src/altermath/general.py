def add(*nums):
    if not nums:
        return None
    r = 0
    for n in nums: 
        r += n
    return r


def subtract(*nums):
    if not nums:
        return None
    r = nums[0]
    for n in nums[1:]: 
        r -= n
    return r


def multiply(*nums):
    if not nums:
        return None
    r = nums[0]
    for n in nums[1:]:
        r *= n
    return r


def divide(*nums):
    if not nums:
        return None
    r = nums[0]
    for n in nums[1:]:
        r /= n
    if isinstance(r, float) and r.is_integer():
        return int(r)
    return r


def mod(*nums):
    if not nums:
        return None
    r = nums[0]
    for n in nums[1:]:
        r %= n
    return r


def fdiv(*nums):
    if not nums:
        return None
    r = nums[0]
    for n in nums[1:]:
        r //= n
    return r


def square(*nums):
    if not nums:
        return None
    r = [n ** 2 for n in nums]
    return r[0] if len(r) == 1 else r


def cube(*nums):
    if not nums:
        return None
    r = [n ** 3 for n in nums]
    return r[0] if len(r) == 1 else r


def power(*nums, exp):
    if not nums:
        return None
    r = [n ** exp for n in nums]
    return r[0] if len(r) == 1 else r


def sqrt(*nums):
    if not nums:
        return None
    r = []
    for n in nums:
        if n < 0:
            r.append(None)
            continue
        x = n ** (1 / 2)
        rounded = round(x)
        if rounded ** 2 == n:
            r.append(rounded)
        else:
            r.append(x)
    return r[0] if len(r) == 1 else r


def root(*nums, index):
    if not nums:
        return None
    if isinstance(index, float) or index < 2:
        return None
    r = []
    for n in nums:
        if mod(index, 2) == 0 and n < 0:
            r.append(None)
            continue
        sign = -1 if n < 0 else 1
        value = abs(n)
        x = value ** (1 / index)
        rounded = round(x)
        if rounded ** index == value:
            r.append(sign * rounded)
        else:
            r.append(sign * x)
    return r[0] if len(r) == 1 else r
