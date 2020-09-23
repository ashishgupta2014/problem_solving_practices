from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.courseDict = defaultdict(list)

        for pair in prerequisites:
            nextCourse, prevCourse = pair[0], pair[1]
            self.courseDict[prevCourse].append(nextCourse)

        self.visitList = defaultdict(lambda: None)
        for course in range(numCourses):
            if not self.visitList[course]:
                if self.dfs(course) == 'CYCLE':
                    return False

        return True

    def dfs(self, course):
        if self.visitList[course] == 'visited': return True
        if self.visitList[course] == 'visiting': return 'CYCLE'

        self.visitList[course] = 'visiting'
        for c in self.courseDict[course]:
            if self.dfs(c) == 'CYCLE': return 'CYCLE'
        self.visitList[course] = 'visited'

        return True
s = Solution()
print(s.canFinish(3, [[1, 0], [0, 2], [2, 1]]))
