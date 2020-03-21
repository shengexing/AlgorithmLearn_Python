""" 快速排序 """

import random


# 快速排序的函数
def quickSort(array):
    if len(array) < 2:
        return array  # 基线条件：为空或只包含一个元素的数组是 “有序” 的
    else:
        index = random.randint(0, len(array) - 1)
        return quickSort(
            [i for i in array[0:index] + array[index+1:] if i < array[index]]
        ) + [array[index]] + quickSort(
            [i for i in array[0:index] + array[index+1:] if i >= array[index]]
        )


print(quickSort([]))
print(quickSort([5]))
print(quickSort([5, 3]))
print(quickSort([5, 3, 6, 2, 10]))
