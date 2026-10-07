class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {}
        for course in prerequisites:
            if course[0] not in courses:
                courses[course[0]] = [course[1]]
            else:
                courses[course[0]].append(course[1])
            

        current = set()
        def dfs(course):
            if course not in courses:
                return True
            if course in current:
                return False
            current.add(course)
            for prereq in courses[course]:
                find_req = dfs(prereq)
                if not find_req:
                    return False
            current.remove(course)
            del courses[course]
            return True
        
        for course in range(0, numCourses):
            curr = dfs(course)
            if not curr:
                return False
        
        return True

            






            

