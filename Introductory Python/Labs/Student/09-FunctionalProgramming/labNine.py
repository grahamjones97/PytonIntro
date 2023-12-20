print((lambda x: x % 2 == 0)(555))  # Works


# def negate(f):
#     f = [1, 2, 3]
#     myneglist = [-x for x in f]
#     return myneglist


# def negative(func):
#     lst = func([])
#     print(lst)


# negative(negate)


def nth(number, list):
    if number == list[0]:
        return list[0]
    else:
        print(list)


my_list = [1, 2, 3, 4]

print(nth(1, my_list))
