"""
1462. Course Schedule IV
https://leetcode.com/problems/course-schedule-iv

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a
prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer
whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.
"""

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = [[] for _ in range(numCourses)]
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        all_prereqs = [set() for _ in range(numCourses)]
        visited = [False]*numCourses
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for v in adj[node]:
                dfs(v)
                all_prereqs[node].add(v)
                all_prereqs[node].update(all_prereqs[v])
            return

        for node in range(numCourses):
            dfs(node)

        result = []
        for u, v in queries:
            result.append(u in all_prereqs[v])

        return result
    
solver = Solution()
print(solver.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
print(solver.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
print(solver.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))