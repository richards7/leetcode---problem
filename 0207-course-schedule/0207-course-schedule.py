class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
       """
        adj = [[] for _ in range(numCourses)]
        deg = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            deg[course] += 1
        q = [i for i in range(numCourses) if deg[i] == 0]
        done = 0
        idx = 0
        while idx < len(q):
            node = q[idx]
            idx += 1
            done += 1
            for nxt in adj[node]:
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    q.append(nxt)
        return done == numCourses