

#递归
class To_factorial:
    """
    递归
    1 定义一个阶乘函数f(x)
    2 明确等级关系 5的阶乘 = 5 * 4的阶乘
    3 明确出口 1的阶乘 = 1
    4 写出函数
    def 阶乘(x):
        if x ==1:
            return 1
        else:
            return x*阶乘(x-1)
    """

    def __init__(self):
        pass


```


```python
# 递归
def unfold_dict(v,host_name):
    for k,v in v.items():
        if isinstance(v,dict):
            host_name = k + '__'
            print('ok')
            unfold_dict(v,host_name=host_name)
        elif isinstance(v,str):
            try:
                json.loads(v)
            except:
                print('ok')
                xx[host_name+k] = v
        else:
            raise "error"
            
```

