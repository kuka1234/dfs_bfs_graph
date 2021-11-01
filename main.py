from collections import defaultdict, deque


# defaultdict: when an element is referenced which is not in dictionary: adds to dictionary rather than error
# Creates graph(directed or undirected), then can use bfs or dfs to find path.

class Graph:
    # creates graph: dictionary, directed: if the graph is directed.
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    # creates edge by appending graph dictionary, creates edge in both direction if graph undirected.
    def addEdge(self, u, v):
        if self.directed:
            self.graph[u].append(v)
        else:
            if v not in self.graph[u]:
                self.graph[u].append(v)
            if u not in self.graph[v]:
                self.graph[v].append(u)


class Search:

    @staticmethod
    def depth_search(igraph, target, starting_point, visited):
        path = []  # final path from start point to end point
        stack = deque()
        stack.append(starting_point)

        while stack:  # if stack not empty
            current_vertex = stack[-1]  # takes last element added from stack
            visited.add(current_vertex)

            if current_vertex not in path:  # if not traversed
                path.append(current_vertex)

            if target != current_vertex:
                # if has no connected vertices or ALL the connected vertices have already been visited
                if len(igraph.graph[current_vertex]) == 0 or all(
                        child_vertex in visited for child_vertex in igraph.graph[current_vertex]):
                    stack.pop()
                    path.remove(current_vertex)  # removes from final path as back tracking
                else:
                    for child_vertex in igraph.graph[current_vertex]:
                        if child_vertex in visited:
                            pass
                        else:
                            stack.append(child_vertex)
            else:
                return path

    @staticmethod
    def breadth_search(igraph, target, current_vertex):
        que = []
        paths = defaultdict(list)  # dictionary of all paths in graph

        while current_vertex != target:
            for child_vertex in igraph.graph[current_vertex]:
                if child_vertex not in paths[current_vertex]:
                    que.append(child_vertex)
                    # key is child_vertex, path up to that vertex is value.
                    paths.update({child_vertex: {current_vertex: paths[current_vertex]}})
            current_vertex = que.pop(0)
        path_dict = {target: paths[target]}  # adds final value to final path.

        # converts path from dictionary into list.
        path = []
        while path_dict:
            for i in path_dict:
                path.append(i)
                path_dict = path_dict[i]
        path.reverse()  # reverses list as order is backwards
        return path


first = Graph(False)
first.addEdge('A', 'B')
first.addEdge('B', 'C')
first.addEdge('C', 'F')
first.addEdge('F', 'C')
first.addEdge('B', 'E')
first.addEdge('E', 'B')
first.addEdge('B', 'D')
first.addEdge('E', 'G')
first.addEdge('G', 'H')
first.addEdge('G', 'I')

search = Search()
path = search.depth_search(first, 'F', 'A', visited=set())
print(path)
path = search.breadth_search(first, 'F', 'A')
print(path)
