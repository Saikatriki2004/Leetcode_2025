class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize the reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Populate direct prerequisites
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Step 3: Apply Floyd-Warshall to compute indirect prerequisites
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        # Step 4: Answer the queries
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result
