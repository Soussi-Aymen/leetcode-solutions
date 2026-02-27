class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph: graph[a][b] = a/b
        graph = {}
        
        # Step 1: Build the graph
        for (dividend, divisor), value in zip(equations, values):
            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}
            
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value  # Reverse edge
        
        # Step 2: DFS to find path and calculate result
        def dfs(start, end, visited):
            # Base cases
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # Explore neighbors
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    # Recursively find path from neighbor to end
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            
            return -1.0
        
        # Step 3: Process each query
        result = []
        for dividend, divisor in queries:
            result.append(dfs(dividend, divisor, set()))
        
        return result