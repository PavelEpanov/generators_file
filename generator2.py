# def get_list():
#     my_list = [1, 2, 3, 4, 5]
#     for x in my_list:
#         yield x
#
# a = get_list()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def average():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)

a = average()
# for x in a:
#     print(x)
print(list(a))
