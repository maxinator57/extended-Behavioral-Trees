from pddl_classes import *
from domain_parser import *

def parse_problem(domain, problem_file):
    try:
        for line in problem_file:
            head = line.split()
            if len(head) != 0:
                break
        for i in range(len(head)):
            head[i] = head[i].strip('(').strip(')')
        P = Problem(head[2])    
        for line in problem_file:
            cur = line.split()
            for i in range(len(cur)):
                cur[i] = cur[i].strip('(').strip(')')            
            if len(cur) != 0 and cur[0] != ':domain':
                break
        domain_name = cur[0]
        if domain_name != domain.name:
            print('Error: given domain is not valid for this problem\n')
            return
        for line in problem_file:
            cur = line.split()
            for i in range(len(cur)):
                cur[i] = cur[i].strip('(').strip(')')
            if len(cur) > 0 and cur[0] == ':objects':
                break
        for obj_name in cur[1:]:
            P.obj.append(Object(obj_name))
        return P
    except:
        print('Wrong format: unable to recognize\n')
        return
    
domain_file = open('domain_example-1.pddl', 'r')
D = parse_Domain(domain_file)
problem_file = open('problem_example-1.pddl', 'r')
P = parse_problem(D, problem_file)