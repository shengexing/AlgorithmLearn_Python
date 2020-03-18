""" 数组元素求和 """


# 对数组中所用元素求和
def sumArray(num):
    if num:
        return num.pop() + sumArray(num)  # 数组不为空，取出最后一个元素
    else:
        return 0  # 数组为空，返回 0


print(sumArray([1, 2, 3, 4, 5, 6]))
