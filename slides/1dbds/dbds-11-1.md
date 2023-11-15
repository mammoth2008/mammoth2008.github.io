11. 图
11.1 图的基本概念

图的定义
由顶点的有穷非空集合和顶点之间边的集合组成
通常表示为 G = (V, E)
V 是图 G 中顶点的集合, 记为 V(G)
E 是图 G 中边的集合, 记为 E(G)

图的抽象数据类型
ADT 图(Graph)
{
    数据对象
    $ D = \lbrace a\_i | 0 \leq i \leq n - 1, n \geq 0, a\_i \in \Sigma \rbrace $
    数据关系
    $ R = \lbrace &lt; a\_i, a\_j &gt; | a\_i, a\_j \in D, 0 \leq i \leq n - 1, 0 \leq j \leq n - 1 \rbrace $
    基本运算
    void CreateGraph()
    void DispGraph()
    ...
}

图的基本术语
顶点 Vertex $ i $
边 Edge $ (i, j) $
无向图 Undirected Graph $ (i, j) $
弧 Arc $ &lt; i, j &gt; $
有向图 Directed Graph $ &lt; i, j &gt; $
