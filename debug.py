from new_domain_parser import *
from problem_parser import *
from grounder import *
from htn_algorithm import *

Domain_file = open('domain_basic.pddl', 'r')
Problem_file = open('problem_basic.pddl', 'r')
D = parse_Domain(Domain_file)
#for task in D.tasks:
 #   print(task, 'task')
  #  for method in D.tasks[task].methods:
   #     print(method.name)
    #    for precond in method.preconds:
     #       print(precond[0].name, precond)
P = parse_Problem(Problem_file)
res = ground(D, P)
seq = []
print(find_solution(res, seq, P.init_state))