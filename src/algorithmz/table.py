
# 基数排序


# LSD Radix Sort
def radix_sort(lst):
    mod = 10
    div = 1
    mostBit = len(str(max(lst)))
    buckets = [[] for row in range(mod)]
    while mostBit:
        for num in lst:
            buckets[num // div % mod].append(num)
        i = 0
        for bucket in buckets:
            while bucket:
                lst[i] = bucket.pop(0)
                i += 1
        div *= 10
        mostBit -= 1
    return lst

%%time
sort_function_check(bucket_sort)



# 栈
class Stack():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

#队列
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)




# 线性表

from abc import ABC, abstractmethod

ssss测试


class ADT(ABC):
    def __init__(self):
        pass

    def Destory(self):
        # 销毁
        pass

    def Clear(self):
        # 重置
        pass

    @staticmethod
    def Empty(L)->bool:
        # 条件: 线性表已存在
        # 判断空
        pass

    @staticmethod
    def Length(L)->int:
        pass

    @staticmethod
    def Traverse(L,visit):
        pass


# 顺表
class List(ADT):
    def __init__(self):
        self.value = None

    def Create(self,value):
        self.value = value

    @staticmethod
    def GetElem(L,i)->int:
        # 条件: 线性表已存在 且 1<=i<=length
        # 返回第i个元素
        assert 1<=i<=List.ListLength(L)

        return L.value[i-1]

    def ListInsert(self,i,e):
        # 条件: 线性表已存在 且 1<=i<=length+1
        # 在第i 个位置之前插入数据 L的长度+1
        self.value.insert(i-1,e)

    def ListDelete(self,i)->'e':
        # 条件: 线性表已存在
        # 删除第i个元素数据 长度减1
        self.value.pop(i-1)

    @staticmethod
    def ListTraverse(L,visit=None):
        # 条件: 线性表已存在
        for i in L.value:
            if visit:
                visit(i)

    # 查找算法
    @staticmethod
    def search(lst,key):
        lst2 = [key] + lst
        for i in range(len(lst2)-1,-1,-1):
            if lst2[i] == key:
                return i
    @staticmethod
    def search_bin(lst,key):
        # 折半查找
        low = 1
        high = len(lst)

        while low <=high:
            mid = (low+high)//2
            if key == lst[mid-1]:
                return mid
            elif key < lst[mid-1]:
                high = mid -1
            else:
                low= mid+1
        return 0

    # 8大排序
    def insert_sort(alist):
        # 从第二个位置，即下标为1的元素开始向前插入
        for i in range(1, len(alist)):
            # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
            for j in range(i, 0, -1):
                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]
    def bin_sort(alist):
        for i in range(1, len(alist)):
            key = alist[i]
            low = 0
            high = i - 1
            while low <= high:  # 二分查找确定插入位置
                mid = (low + high) // 2
                if key < alist[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            for j in range(i, low, -1):  # 移动元素腾出空间
                alist[j] = alist[j - 1]
            alist[low] = key  # 插入元素
        return alist

    # 冒泡排序

    def bubble_sort(alist):
        n = len(alist)
        for i in range(n):
            for j in range(0, n-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist


    def quicksort(alist):
        # 快速排序
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort(arr, low, pi-1)
                quick_sort(arr, pi+1, high)
            return arr
        quick_sort(alist,0,len(alist)-1)
    def selectionSort(alist):
        #选择排序
        for i in range(len(alist) - 1):
            # 记录最小数的索引
            minIndex = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[minIndex]:
                    minIndex = j
            # i 不是最小数时，将 i 和最小数进行交换
            if i != minIndex:
                alist[i], alist[minIndex] = alist[minIndex], alist[i]
        return alist


    def heapsort(arr):
        # 堆排序
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heap_sort(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
            return arr
        heap_sort(arr)

    def shellSort(arr):
        # 希尔排序
        n = len(arr)
        # 这里的gap取什么是根据你的实际状况取最优，为了展示方便，选择了取半
        gap = n // 2
        while gap > 0:
            for i in range(gap,n):
                j = i
                while j > 0:
                    # 到这里就很插入有不一样的地方了，对比的不是-1，而是减去步长
                    if arr[j] < arr[j-gap]:
                        arr[j], arr[j-gap] = arr[j-gap], arr[j]
                        # 这里也是同理
                        j -= gap
                    else:
                        break
            # 然后在进行分组 直到 while的gap不是为0为止
            gap //= 2
        return arr

    def radix_sort(arr):
        # 基数排序
        # 计算最大位数
        max_num = max(arr)
        digits = len(str(max_num))

        for i in range(digits):
            # 创建空桶
            buckets = [[] for _ in range(10)]

            # 将元素分配到桶中
            for num in arr:
                index = (num // 10**i) % 10
                buckets[index].append(num)

            # 合并桶
            arr = []
            for bucket in buckets:
                arr.extend(bucket)

        return arr

    def mergesort(arr):
        # 归并排序
        def merge(left,right):
            result = []
            while left and right:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0));
            while left:
                result.append(left.pop(0))
            while right:
                result.append(right.pop(0));
            return result
        def mergeSort(arr):
            import math
            if(len(arr)<2):
                return arr
            middle = math.floor(len(arr)/2)
            left, right = arr[0:middle], arr[middle:]
            return merge(mergeSort(left), mergeSort(right))

        return mergeSort(arr)


# 链
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DNode:
    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.prev = None
        self.next = None


# 链表
class LinkList(ADT):
    def __init__(self):
        self.head = Node(0)

    def CreateHead(self,value):
        for i in value:
            p = Node(i)
            p.next = self.head.next
            self.head.next = p

            self.head.data +=1

    def CreateTail(self,value):
        p = self.head
        for i in value:
            p.next = Node(i)
            p = p.next

            self.head.data +=1

    def _getNode(self,i)->Node:
        p = self.head.next
        j = 1
        while j<i-1:
            p = p.next
            j+=1
        return p

    @staticmethod
    def GetElem(L,i)->int:
        # 条件: 线性表已存在 且 1<=i<=length
        # 返回第i个元素
        assert 1<=i<=L.head.data
        p = L._getNode(i+1)
        return p.data

    def ListInsert(self,i,e):
        # 条件: 线性表已存在 且 1<=i<=length+1
        # 在第i 个位置之前插入数据 L的长度+1
        assert 1<=i<=self.head.data+1
        p = self._getNode(i)
        new_node = Node(e)
        new_node.next = p.next
        p.next = new_node
        self.head.data +=1

    def ListDelete(self,i)->'e':
        # 条件: 线性表已存在
        # 删除第i个元素数据 长度减1
        assert 1<=i<=self.head.data
        p = self._getNode(i)
        p.next = p.next.next
        self.head.data -=1

    @staticmethod
    def ListTraverse(L,visit=None):
        # 条件: 线性表已存在
        p = L.head
        while p.next:
            p = p.next
            if visit:
                visit(p.data)

# 循环链表
class CircularLinkList(LinkList):
    def __init__(self):
        self.head = Node(0)
        self.head.next = self.head

    def CreateTail(self,value):
        p = self.head
        for i in value:
            p.next = Node(i)
            p = p.next
            p.next = self.head #// 有链表新增 //
            self.head.data +=1

    @staticmethod
    def ListTraverse(L,visit=None):
        # 条件: 线性表已存在
        p = L.head
        while p.next!=L.head:# TODO p.next  解决循环尾端的问题
            p = p.next
            if visit:
                visit(p.data)

# 双向链表
class DoublyLinkList(LinkList):
    def __init__(self):
        self.head = DNode(0)

    def CreateHead(self,value):
        for i in value:
            p = DNode(i)
            p.prov = self.head
            p.next = self.head.next

            self.head.next = p

            if p.next:          # TODO
                p.next.prov = p # TODO
            self.head.data +=1

    def CreateTail(self,value):
        p = self.head
        for i in value:
            p.next = DNode(i)
            p.next.prov = p # TODO
            p = p.next
            self.head.data +=1

    def ListInsert(self,i,e):
        # 条件: 线性表已存在 且 1<=i<=length+1
        # 在第i 个位置之前插入数据 L的长度+1
        assert 1<=i<=self.head.data+1
        p = self._getNode(i)
        new_node = DNode(e) # TODO
        new_node.prov = p  # TODO
        new_node.next = p.next
        p.next = new_node
        new_node.next.prov = new_node # TODO

        self.head.data +=1

    def ListDelete(self,i)->'e':
        # 条件: 线性表已存在
        # 删除第i个元素数据 长度减1
        assert 1<=i<=self.head.data
        p = self._getNode(i)
        p.next = p.next.next
        p.next.prov = p      # TODO
        self.head.data -=1


# 栈和队列

# 顺序栈

class Stack(ADT):
    def __init__(self,stacksize = 10):
        # 初始化一个空栈

        self.store = [None]*stacksize
        self.stacksize = stacksize
        self.top = 0
        self.base = 0

    def Create(self,value):
        for i in value:
            self.Push(i)

    @staticmethod
    def GetTop(S)->'data':
        # 栈存在且非空
        # 查看栈顶元素
        assert not S.top == S.base
        e = S.store[S.top -1]
        return e

    def Push(self,e):
        # 栈存在
        # 压栈
        if self.top - self.base >=self.stacksize:
            # 扩容
            self.store += [None]*10
            self.stacksize +=10

        self.store[self.top] = e
        self.top +=1


    def Pop(self)->'data':
        # 栈存在
        # 弹出栈顶元素
        assert not self.top == self.base
        self.top -=1
        e = self.store[self.top]
        return e

    @staticmethod
    def StackTraverse(S,visit):
        # 遍历
        for i in S.store[:S.top]:
            if visit:
                visit(i)


# 循环队列
class CriQueue(ADT):
    def __init__(self,queuesize = 10):
        # 初始化一个空栈

        self.store = [None]*queuesize
        self.queuesize = queuesize
        self.front = 0
        self.rear = 0

    @staticmethod
    def GetHead(Q)->'data':
        # 存在且非空
        # 查看队头元素
        assert not Q.rear == Q.front
        e = Q.store[Q.front]
        return e

    @staticmethod
    def QueueLength(Q):
        return (Q.rear - Q.front + Q.queuesize)% Q.queuesize


    def EnQueue(self,e):
        # 存在
        # 插入队尾元素
        print(self.rear,self.front,self.queuesize)
        assert (self.rear + 1) % self.queuesize != self.front
        self.store[self.rear] = e
        self.rear = (self.rear+1) % self.queuesize


    def DeQueue(self)->'data':
        # 存在
        # 删除队头元素
        assert not self.front == self.rear
        e = self.store[self.front]
        self.front = (self.front+1) % self.queuesize
        return e

    @staticmethod
    def StackTraverse(S,visit):
        # 遍历
        for i in S.store[:S.top]:
            if visit:
                visit(i)


# 链队列
class LinkQueue(LinkList):
    def __init__(self):
        # 初始化一个空队列
        self.front = self.rear = Node(0)
        self.head = self.front

    @staticmethod
    def GetHead(Q)->'data':
        e = Q.head.next.data
        return e

    def EnQueue(self,e):
        # 存在
        # 插入队尾元素
        new_node = Node(e)
        self.rear.next = new_node
        self.rear = new_node
        self.head.data +=1


    def DeQueue(self)->'data':
        # 存在
        # 删除队头元素
        assert not self.front == self.rear
        p = self.front.next
        e = p.data
        self.front.next = p.next
        self.front.data -= 1
        if self.rear == p:
            self.rear = self.front
        return e


def Index(S,T):
    # 模式匹配 暴力匹配
    n = len(S)
    m = len(T)
    if m == 0:
        return 0
    i = 1
    while i <(n-m+1):
        for j in range(m):
            if S[i+j] != T[j]:
                # print('失败')
                break
        else:
            # print('匹配成功')
            return i
        i+=1
    return 0

