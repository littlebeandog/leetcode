# num of courses seems redundante param in this case?
# here's the AC code
from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacent_list = defaultdict(list)
        for tail, head in prerequisites:
            adjacent_list[head].append(tail)

        is_visit = defaultdict(int)
        for vertex in adjacent_list:
            if not self.dfs(adjacent_list, is_visit, vertex):
                return False
        return True

    def dfs(self, adjacent, is_visit, vertex):
        # 1: visited in other dfs
        # 0: not visited
        # 2: being visited in current dfs recursion
        if is_visit[vertex] == 2:
            return False
        if is_visit[vertex] == 1:
            return True
        is_visit[vertex] = 2
        if vertex in adjacent:
            for one_vertex in adjacent[vertex]:
                if not self.dfs(adjacent, is_visit, one_vertex):
                    return False
        is_visit[vertex] = 1
        return True