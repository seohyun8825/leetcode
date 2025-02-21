class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set() 
        visited = set() 

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)

            visited.add(i)
            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True
