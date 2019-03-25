from new_domain_parser import *


def parse_obj_tokens(tokens, start, Problem):
    if start >= len(tokens):
        if start > 0:
            return True
        else:
            return False
    if tokens[start] == ')':
        return False    
    for i in range(start, len(tokens)):
        (Problem.objects).append(tokens[i].strip('(').strip(')'))
    return (not tokens[-1][-2:] == '))')


def parse_objects(Problem_file, Problem):
    line = skip_empty_lines(Problem_file)
    tokens = line.split()
    if tokens[0] != '(:objects':
        print('Bad format objects\n')
        return
    start = 1
    while parse_obj_tokens(tokens, start, Problem):
        tokens = skip_empty_lines(Problem_file).split()
        start = 0
        
        
def parse_state_pred_tokens(tokens, start, state):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False
    predname = ''
    objects = []
    f = 1
    for j in range(start, len(tokens)):
        if f:
            predname = tokens[j].strip('(').strip(')')
            objects.clear()
            f = 0
        else:
            objects.append(tokens[j].strip(')'))
        if tokens[j][-1] == ')':
            if predname not in state.preds.keys():
                state.preds[predname] = Predicate(predname, len(objects), [])
            state.preds[predname].params.append(objects.copy())
            f = 1
    return (not tokens[-1][-2:] == '))')


def parse_init_preds(Problem_file, Problem):
    line = skip_empty_lines(Problem_file)
    tokens = line.split()
    if tokens[0] != '(:init':
        print('Bad format: init predicates\n')
        return
    start = 1
    while parse_state_pred_tokens(tokens, start, Problem.init_state):
        tokens = skip_empty_lines(Problem_file).split()
        start = 0
        
        
def parse_goal_tokens(tokens, start, Problem):
    if start >= len(tokens):
        if start > 0:
            return True
        else:
            return False
    if tokens[start] == ')':
        return False
    taskname = ''
    objects = []
    f = 1
    for j in range(start, len(tokens)):
        if f:
            taskname = tokens[j].strip('(').strip(')')
            objects = [taskname]
            f = 0
        else:
            objects.append(tokens[j].strip(')'))
        if tokens[j][-1] == ')':
            Problem.goals.append(objects.copy())
            f = 1
    return (not tokens[-1][-2:] == '))')  


def parse_goals(Problem_file, Problem):
    line = skip_empty_lines(Problem_file)
    tokens = line.split()
    if tokens[0] != '(:goals':
        print('Bad format goals\n')
        return
    start = 1
    while parse_goal_tokens(tokens, start, Problem):
        tokens = skip_empty_lines(Problem_file).split()
        start = 0    


def parse_Problem(Problem_file):
    P = Problem()
    headline = skip_empty_lines(Problem_file)
    P.name = headline[2][:-1]
    P.domain_name = skip_empty_lines(Problem_file)[1][:-1]
    parse_objects(Problem_file, P)
    parse_init_preds(Problem_file, P)
    parse_goals(Problem_file, P)
    return P