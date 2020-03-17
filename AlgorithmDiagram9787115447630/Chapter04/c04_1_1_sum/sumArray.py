""" 数组元素求和 """


# 对数组中所用元素求和
def sumArray(num):
    if len(num) == 0:
        return 0
    else:
        return num.pop() + sumArray(num)


print(sumArray([1, 2, 3, 4, 5, 6]))
