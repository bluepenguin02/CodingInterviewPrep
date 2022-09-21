"""
https://leetcode.com/problems/course-schedule-ii/

210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = self.build_graph(numCourses, prerequisites)
        order = []

        # Note: would be more efficient to use an array that serves the purpose of
        # all_visited and curr_stack_set
        all_visited = set()
        curr_stack_set = set()
        found_cycle = False

        def dfs(node: int):
            nonlocal found_cycle
            if node in curr_stack_set:
                found_cycle = True
                return

            if node in all_visited:
                return

            curr_stack_set.add(node)
            for v in graph[node]:
                dfs(v)
            all_visited.add(node)
            order.append(node)
            curr_stack_set.discard(node)
            return

        for node in range(numCourses):
            dfs(node)
            if found_cycle:
                return []

        order.reverse()
        return order
      

    def build_graph(self, numCourses, prerequisites) -> list[list[int]]:
        graph = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)
        return graph