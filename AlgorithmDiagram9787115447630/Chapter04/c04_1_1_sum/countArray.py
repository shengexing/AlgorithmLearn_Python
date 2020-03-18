""" 列表元素求总数 """


# 对列表元素求总数
def countArray(num):
    if num:
        num.pop()  # 数组不为空，取出最后一个元素
        return 1 + countArray(num)
    else:
        return 0  # 数组为空，返回 0


print(countArray([1, 2, 3, 4, 5, 6]))
