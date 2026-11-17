class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preq = {i: [] for i in range(numCourses)}
        for cou, pre in prerequisites:
            preq[cou].append(pre)

        visited=set()

        def dfs(cou):

            if cou in visited:
                return False

            if preq[cou]==[]:
                return True
            
            visited.add(cou )

            for pre in preq[cou]:

                if not dfs(pre):
                    return False
            visited.remove(cou)
            preq[cou]=[]
            return True
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True

            
        