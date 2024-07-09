class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for key, value in self.adj_list.items():
            print(f"{key} : {value}")
    
    def add_vertex(self, value):
        if value in self.adj_list:
            return False
        self.adj_list[value] = []
        return True
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 in self.adj_list[vertex1]:
                self.adj_list[vertex1].remove(vertex2)
            if vertex1 in self.adj_list[vertex2]:
                self.adj_list[vertex2].remove(vertex1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False
        edges = self.adj_list[vertex]
        self.adj_list.pop(vertex)
        for key in edges:
            self.adj_list[key].remove(vertex)
        return True