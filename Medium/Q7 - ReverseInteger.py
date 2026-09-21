def reverse(x: int) -> int:
    rev = None
    if (x < 0):
        x *= -1
        rev = str(x)[::-1]
        rev = int(rev) * (-1)

    else:
        rev = str(x)[::-1]
        rev = int(rev)

    if ((-2 ** 31) < int(rev) < (2 ** 31)):
        return rev
    else:
        return 0

