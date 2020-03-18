""" 数组元素求和 """


# 对数组中所用元素求和
def sumArray(num):
    if num:
        return num.pop() + sumArray(num)
    else:
        return 0


print(sumArray([1, 2, 3, 4, 5, 6]))
