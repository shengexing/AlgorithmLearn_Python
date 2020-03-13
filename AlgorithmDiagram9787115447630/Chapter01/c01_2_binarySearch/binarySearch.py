""" 二分查找 """


def binary_search(list, item):
    # low 和 high 用于跟踪要在其中查找的列表部分
    low = 0
    high = len(list) - 1

    while low <= high:  # 只要范围没有缩小到只包含一个元素，
        mid = int((low + high) / 2)  # 就检查中间元素
        guess = list[mid]
        if guess == item:  # 找到了元素
            return mid
        if guess > item:  # 猜的数字大了
            high = mid - 1
        else:  # 猜的数字小了
            low = mid + 1
    return None  # 没有指定的元素


my_list = [1, 3, 5, 7, 9]  # 来测试一下

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None
