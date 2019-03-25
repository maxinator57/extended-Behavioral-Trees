from htn_classes import *

def ground(Domain, Problem):
    res = []
    for goal in Problem.goals:
        # print(goal)
        task = Domain.tasks[goal[0]]
        res.append(task_node(task, goal[1:]))
    return res