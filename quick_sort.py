# 快速排序
# 原始数据 -value
# [80, 70, 90, 54, 78, 42, 79, 93, 53, 71]

def quick_sort(value):
    # 递归退出条件
    if len(value) < 2:
        return value

    # 设置一个关键数据
    mark = value[0]
    # 找出所有小于关键数据的
    small = [x for x in value if x < mark]
    # 找出所有等于关键数据的
    equal = [x for x in value if x == mark]
    # 找出所有大于关键数据的
    big = [x for x in value if x > mark]

    # 从小到大顺序拼接
    return quick_sort(small) + equal + quick_sort(big)


if __name__ == "__main__":
    lst = [80, 70, 90, 54, 78, 42, 79, 93, 53, 71]
    print(quick_sort(lst))
