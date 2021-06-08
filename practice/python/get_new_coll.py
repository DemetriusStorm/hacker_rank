
def _fail2(coll, *values):
    excluded = []
    result = []
    for element in coll:
        if element not in values:
            result.append(element)
        else:
            if element in excluded:
                result.append(element)
            else:
                excluded.append(element)
    return result


current = [1, 2, 3, 4, 5]
print(_fail2(current))
print(_fail2(current, []))
print(_fail2(current, None))
print(_fail2(current, 9))


