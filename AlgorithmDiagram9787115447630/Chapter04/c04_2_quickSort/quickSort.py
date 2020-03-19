""" 快速排序 """


# 快速排序的函数
def quickSort(array):
    if len(array) < 2:
        return array  # 基线条件：为空或只包含一个元素的数组是 “有序” 的
    else:
        return quickSort([i for i in array[1:] if i < array[0]]) + \
               [array[0]] + \
               quickSort([i for i in array[1:] if i >= array[0]])


print(quickSort([]))
print(quickSort([5]))
print(quickSort([5, 3]))
print(quickSort([5, 3, 6, 2, 10]))

