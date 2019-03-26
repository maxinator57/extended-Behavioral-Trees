from new_domain_parser import *
from problem_parser import *
from grounder import *
from htn_algorithm import *
from eBT_algorithm import *

Domain_file = open('domain_cubes.pddl', 'r')
Problem_file = open('problem1.pddl', 'r')
D = parse_Domain(Domain_file)
P = parse_Problem(Problem_file, D)
res = ground(D, P)
plan = find_htn_solution(res, P.init_state)
if len(plan) == 0:
    print('\nNo solutions found')
else:
    opline = []
    print('\nPlan created:\n')
    length = 0
    for call in plan:
        op_node = call[0].methods[call[1] - 1]
        if call[0].task.primitive:
            opline.append(call)
            print(op_node.method.name, op_node.args)
            length += 1
    print('\nof length', length, end='\n')
    #for block in eBT_go(opline):
     #   print(block)