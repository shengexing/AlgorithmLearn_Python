""" 列表元素求总数 """


# 对列表元素求总数
def countArray(num):
    if num:
        num.pop()
        return 1 + countArray(num)
    else:
        return 0


print(countArray([1, 2, 3, 4, 5, 6]))
