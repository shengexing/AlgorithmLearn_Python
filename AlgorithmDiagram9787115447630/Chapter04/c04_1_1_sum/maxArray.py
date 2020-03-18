""" 列表元素找最大数 """


# 对列表元素求最大值
def maxArray(num):
    if num:
        temp0 = num.pop()
        if num:
            temp1 = maxArray(num)
            if temp0 < temp1:
                return temp1
        return temp0
    else:
        return None


print(maxArray([]))
print(maxArray([7]))
print(maxArray([1, 2, 9, 4, 3, 6]))
