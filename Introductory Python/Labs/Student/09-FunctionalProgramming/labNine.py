print((lambda x: x % 2 == 0)(555))  # Works


# def negate(f):
#     f = [1, 2, 3]
#     myneglist = [-x for x in f]
#     return myneglist


# def negative(func):
#     lst = func([])
#     print(lst)


# negative(negate)


def nth(number, mylist):
    if mylist != number:
        return mylist[number]
    return 1 + nth(mylist[1:], number)


my_list = [100, 101, 102, 103, 104, 105, 106]
print(nth(3, my_list))
