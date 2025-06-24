



# 图

图
	CreateGraph(\&G,V,VR);
		初始条件： V 是图的顶点集， VR 是图中弧的集合。
		操作结果：按 V和VR的定义构造图G。
	LocateVex (G, U)；
		初始条件：图 G 存在， u 和 G 中顶点有相同特征。
		操作结果：若 G 中存在顶点 u ，则返回该顶点在图中位置；否则返回其他信息。
	GetVex(G, v);
		初始条件：图 G存在， V 是 G 中某个顶点。
		操作结果：返回 V 的值。
	DFSTraverse(G, Visit())；
		初始条件：图 G 存在，Visit 是顶点的应用函数。
		操作结果：对图进行深度优先遍历。在遍历过程中对每个顶点调用函数 Visit 一次且仅一次。一旦 visit（）失败，则操作失败。
		深度优先搜索
		使用栈
	BFSTraverse(G, Visit())；
		初始条件：图G存在, Visit 是顶点的应用函数。
		操作结果：对图进行广度优先遍历。在遍历过程中对每个顶点调用函数 Visit 一次且仅一次。一旦 visit(）失败，则操作失败。
		广度优先搜索
		做一个标志用来看节点是否被访问过
		使用队列
```



VOE网

- AOV
    
    - 定义
        
        - 在这种有向图中,顶点表示活动,边表示活动的优先关系 Action on Vertices
            
        - 直接前驱,直接后继
            
        - 反自反性
            
        - 不能出现环
            
    - 对规定的AOV网
        
        - 要先判断它是否有环, 方法是对它进行拓扑排序, 将其顶点排列成线性有序序列, 若该序列中包含全部顶点, 则无环,
            
    - 拓扑排序的步骤
        
        - 在AOV网中选择一个入度为0的顶点且输出
            
        - 从AOV网中删除该顶点和该顶点发出的所有有向边
            
        - 重复, 直到AOV网中所有顶点都被输出或网中不存在入度为0的顶点








https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_linear_regression/#summary


https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial11/NF_image_modeling.html#



