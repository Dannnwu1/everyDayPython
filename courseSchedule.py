from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Using graph and recursive DFS
        :param numCourses:
        :param prerequisites:
        :return:
        """
        courses = prerequisites
        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * numCourses
        graph = defaultdict(list)
        for u, v in courses:
            graph[u].append(v)

        def dfs(node):
            if status[node] == VISITED:
                return True
            if status[node] == VISITING:
                return False
            status[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            status[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    so = Solution()
    print(so.canFinish(numCourses, prerequisites))
