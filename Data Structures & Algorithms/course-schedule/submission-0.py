from collections import defaultdict, deque
class Solution:
 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The pair [0, 1], indicates that must take course 1 before taking course 0.
        courseToPrereqs = defaultdict(set)
        prereqsToCourses = defaultdict(set)
        for course, prereq in prerequisites:
            courseToPrereqs[course].add(prereq)
            prereqsToCourses[prereq].add(course)
            
            if not prereq in courseToPrereqs:
                courseToPrereqs[prereq] = set()
            if not course in prereqsToCourses:
                prereqsToCourses[course] = set()

        print("courseToPrereqs", courseToPrereqs)
        print("prereqsToCourses", prereqsToCourses)
        
        q = deque()
        for course, prereqs in courseToPrereqs.items():
            if len(prereqs) == 0:
                q.append(course)

        print(q)
        while q:
            course = q.pop()
            del courseToPrereqs[course]
            for followUpCourse in prereqsToCourses[course]:
                courseToPrereqs[followUpCourse].remove(course)
                if not courseToPrereqs[followUpCourse]:
                    q.append(followUpCourse)
        return not courseToPrereqs