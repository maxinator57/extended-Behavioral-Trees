from new_domain_parser import *
from problem_parser import *
from grounder import *
from htn_algorithm import *

Domain_file = open('domain_hard.pddl', 'r')
Problem_file = open('problem_hard.pddl', 'r')
D = parse_Domain(Domain_file)
#for task in D.tasks:
 #   print(task, 'task')
  #  for method in D.tasks[task].methods:
   #     print(method.name)
    #    for precond in method.preconds:
     #       print(precond[0].name, precond)
P = parse_Problem(Problem_file)
res = ground(D, P)
plan = find_solution(res, P.init_state)
if len(plan) == 0:
    print('No solutions found')
else:
    print('Plan created:')
    for call in plan:
        op_node = call[0].methods[call[1] - 1]
        if call[0].task.primitive:
            print(op_node.method.name, op_node.args)