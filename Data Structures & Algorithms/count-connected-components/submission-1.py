class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        nodes = {}
        for i in range(n):
            nodes[i] = [0]

        for edge in edges:
            if edge[1] not in nodes:
                nodes[edge[1]] = [edge[0]]
            else:
                nodes[edge[1]].append(edge[0])
        
        for edge in edges:
            if edge[0] not in nodes:
                nodes[edge[0]] = [edge[1]]
            else:
                nodes[edge[0]].append(edge[1])
        
        # dfs:
        # we don't care if the graph has a cycle or not
        # we only care to see all the nodes in a given graph
        # use current to track current part of graph
        # use num_connect to count number or graph parts

        current = set()
        num_connect = 0
        def dfs(node):
            if node in current:
                return

            current.add(node)

            for i in nodes[node]:
                dfs(i)

            return 
        
        # iterate over all the nodes to catch diff graphs
        for i in range(0, n):
            if i not in current:
                num_connect += 1
            dfs(i)
        
        return num_connect


            





        

            