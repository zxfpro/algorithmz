
插入排序

折半插入排序

希尔排序




概念
维护一个窗口  有左右两个指针
扩大和缩小窗口


性质
基本用于数组或字符串问题, 解决子数组或子串相关的问题
通常可以将时间复杂度从 n方 优化到 n



边的添加和删除

顶点的添加和删除

初始化



```python

import numpy as np
def sort_function_check(func):
    for i in range(1000):
        datas = np.random.randint(1,10,(100)).tolist()
        answer = np.sort(datas).tolist()
        our_answer = func(datas)
        assert answer == our_answer
    return 'pass check'

# 冒泡排序

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst

%%time
sort_function_check(bubble_sort)

# 选择排序

def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

%%time
sort_function_check(selection_sort)

# 快速排序

def quick_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    baseline = lst[0]
    left = [lst[i] for i in range(1, len(lst)) if lst[i] < baseline]
    right = [lst[i] for i in range(1, len(lst)) if lst[i] >= baseline]
    return quick_sort(left) + [baseline] + quick_sort(right)

%%time
sort_function_check(quick_sort)


# 归并排序

def merge_sort(lst):
    def merge(left,right):
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)


%%time
sort_function_check(merge_sort)

# 堆排序

def heap_sort(lst):
    def adjust_heap(lst, i, size):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest_index = i
        if left_index < size and lst[left_index] > lst[largest_index]:
            largest_index = left_index
        if right_index < size and lst[right_index] > lst[largest_index]:
            largest_index = right_index
        if largest_index != i:
            lst[largest_index], lst[i] = lst[i], lst[largest_index]
            adjust_heap(lst, largest_index, size)

    def built_heap(lst, size):
        for i in range(len(lst )/ /2)[::-1]:
            adjust_heap(lst, i, size)

    size = len(lst)
    built_heap(lst, size)
    for i in range(len(lst))[::-1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)
    return lst


%%time
sort_function_check(heap_sort)

# 插入排序

def insertion_sort(lst):
    for i in range(len(lst) - 1):
        cur_num, pre_index = lst[i+1], i
        while pre_index >= 0 and cur_num < lst[pre_index]:
            lst[pre_index + 1] = lst[pre_index]
            pre_index -= 1
        lst[pre_index + 1] = cur_num
    return lst

%%time
sort_function_check(insertion_sort)

#希尔排序

def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
                else:
                    break
        gap //= 2
    return lst

%%time
sort_function_check(shell_sort)

# 计数排序

def counting_sort(lst):
    nums_min = min(lst)
    bucket = [0] * (max(lst) + 1 - nums_min)
    for num in lst:
        bucket[num - nums_min] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            lst[i] = j + nums_min
            bucket[j] -= 1
            i += 1
    return lst

%%time
sort_function_check(counting_sort)

#桶排序

def bucket_sort(lst, defaultBucketSize=4):
    maxVal, minVal = max(lst), min(lst)
    bucketSize = defaultBucketSize
    bucketCount = (maxVal - minVal) // bucketSize + 1
    buckets = [[] for i in range(bucketCount)]
    for num in lst:
        buckets[(num - minVal) // bucketSize].append(num)
    lst.clear()
    for bucket in buckets:
        bubble_sort(bucket)
        lst.extend(bucket)
    return lst


%%time
sort_function_check(bucket_sort)
