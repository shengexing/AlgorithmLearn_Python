""" 列表元素找最大数 """


# 对列表元素求最大值
def maxArray(num):
    temp0 = num.pop()
    if num:
        temp1 = maxArray(num)
        if temp0 < temp1:
            return temp1
    return temp0


print(maxArray([1, 2, 3, 4, 5, 6]))
