#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Node:
  
    def __init__(self, data, indexloc = None):
        self.data = data
        self.index = indexloc
               
class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

  
    def __init__(self, row, col, nodes = None):
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i


    def connect_dir(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight
  

    def connect(self, node1, node2, weight = 1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if self.adj_mat[node][col_num] != 0]

    def connections_to(self, node):
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_mat]
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]
     
  
    def print_adj_mat(self):
        for row in self.adj_mat:
            print(row)
  
    def node(self, index):
        return self.nodes[index]
    
  
    def remove_conn(self, node1, node2):
        self.remove_conn_dir(node1, node2)
        self.remove_conn_dir(node2, node1)
   
    def remove_conn_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = 0   
  
    def can_traverse_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2] != 0  
  
    def has_conn(self, node1, node2):
        return self.can_traverse_dir(node1, node2) or self.can_traverse_dir(node2, node1)
  
    def add_node(self,node):
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adj_mat:
            row.append(0)     
        self.adj_mat.append([0] * (len(self.adj_mat) + 1))

    def get_weight(self, n1, n2):
        node1, node2 = self.get_index_from_node(n1), self.get_index_from_node(n2)
        return self.adj_mat[node1][node2]

    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index
        
    def dijkstra(self, node):
        nodenum = self.get_index_from_node(node)
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([self.nodes[nodenum]])
        
        dist[nodenum][0] = 0
        queue = [i for i in range(len(self.nodes))]
        seen = set()
        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue: 
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            
            queue.remove(min_node)
            seen.add(min_node)
            connections = self.connections_from(min_node)
            for (node, weight) in connections: 
                tot_dist = weight + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist


# In[44]:


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")

graph = Graph.create_from_nodes([a,b,c,d,e,f,g,h,i,j])

graph.connect(a,b,5)
graph.connect(a,e,6)
graph.connect(b,c,4)
graph.connect(e,d,4)
graph.connect(e,g,5)
graph.connect(g,j,8)
graph.connect(g,h,2)
graph.connect(d,f,3)
graph.connect(f,i,7)

print("Матрица смежности:")
graph.print_adj_mat()


# In[48]:


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")

w_graph = Graph.create_from_nodes([a,b,c,d,e,f,g,h,i,j])

w_graph.connect(a,b,5)
w_graph.connect(a,e,6)
w_graph.connect(b,c,4)
w_graph.connect(e,d,4)
w_graph.connect(e,g,5)
w_graph.connect(g,j,8)
w_graph.connect(g,h,2)
w_graph.connect(d,f,3)
w_graph.connect(f,i,7)

print("Ответ (в последней скобке(длинна пути, вершины)):")
print([(weight, [n.data for n in node]) for (weight, node) in w_graph.dijkstra(a)])


# In[ ]:




