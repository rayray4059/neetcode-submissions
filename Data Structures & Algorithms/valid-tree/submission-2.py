class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and edges == []:
            return True

        nodes = {}
        for node in edges:
            if node[0] not in nodes:
                nodes[node[0]] = [node[1]]
            else:
                nodes[node[0]].append(node[1])
        
        for node in edges:
            if node[1] not in nodes:
                nodes[node[1]] = [node[0]]
            else:
                nodes[node[1]].append(node[0])
        
        current = set()
        def dfs(node, prev):
            if node in current:
                return False
            current.add(node) 
            for i in nodes[node]:
                if i == prev:
                    continue
                out = dfs(i, node)
                if not out:
                    return False
            return True
        
        run_dfs = dfs(0,0)
        return len(current) == n and run_dfs
            



            
            
