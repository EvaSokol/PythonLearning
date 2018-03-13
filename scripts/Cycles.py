# for j in 'hello world':
#     if j == 'a':
#         break
#     print(j, end='')
# else:
#     print("There is no \"a\" in this word")
#
#
# d = dict.fromkeys(['a', 'b', 'c'], "world")
# print(d)
# print(d.popitem())
# print(d)
#
# s = {x*2 for x in range(10)}
# print(s)


# def func(x, y=7):
#     def add(a):
#         print('a=', a)
#         return x + a
#     print('x=', x, y)
#     return add
#
#
# test = func(4, 5)
# # print(test)
# test(8)

# def multi_param(**ddd):
#     print(ddd)
#
#
# print(multi_param(a=6, b=7, c=5))

x = input("Input number ")
print(x)