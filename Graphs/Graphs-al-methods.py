# Graphs - all methods
# Considering non-weigthed and non-directional edges
# Using Adjecency List method. Python Dictionary of Lists. 
# Alternative could be Adjecency Matrix.

class Graph():
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,':',self.adj_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        else:
            return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        else:
            return False
        
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        else:
            return False
        
    def remove_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            return False
        for vertices in self.adj_list[vertex]:
            #print(vertices)
            self.adj_list[vertices].remove(vertex)
        del self.adj_list[vertex]
        return True
            
G = Graph()
G.add_vertex('A')
G.add_vertex('B')
G.add_vertex('C')
G.add_vertex('D')

G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('D','A')
G.add_edge('A','C')
G.add_edge('B','D')
G.print_graph()

print(' Remove Vertex C')
G.remove_edge('A','C')
G.remove_vertex('C')
G.print_graph()
