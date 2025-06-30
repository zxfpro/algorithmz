# 算法

class Core:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        
    def __lt__(self,other):
        print('小于')
        return True
    
    def __gt__(self,other):
        print('大于')
        return False
    
    def __eq__(self,other):
        print('等于')
        return True


a = Core(1,2)
b = Core(2,3)

a==b

a>b



import re
class Infos:
    def __init__(self, key,value):
        self.key = key
        self.value = value
    
    def transform_key(self,key):
        # 使用正则表达式匹配并替换
        new_key = re.sub(r'(\w+)\[\d+\]', r'\1_list', key)
        return new_key

    def __eq__(self, other):
        # 自定义相等
        if isinstance(other, MyClass):
            key = self.transform_key(self.key)
            other_key = self.transform_key(other.key)

            return (key == other_key) and (type(self.value)==type(other.value))
        return False
    
    def __hash__(self):
        # 修改 set 中的值 {}
        return hash(self.transform_key(self.key) + str(type(self.value)))


class Student:
    __slots__ = ('name', 'age', 'score')
    def __init__(self, name, age):
        self.name = name
        self.age = age
