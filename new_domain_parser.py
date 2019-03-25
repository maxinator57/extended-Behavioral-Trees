from htn_classes import *


def skip_empty_lines(Domain_file):
    for line in Domain_file:
        if len(line.strip()) > 0:
            return line
    return ''


def parse_pred_tokens(tokens, start, Domain):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False    
    i = start
    while i < len(tokens):
        pred_name = tokens[i].strip('(').strip(')')
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            j += 1
        arity = j - i - 1
        Domain.preds[pred_name] = Predicate(pred_name, arity)
        i = j
    return (not tokens[-1][-2:] == '))')


def parse_predicates(Domain_file, Domain):
    line = skip_empty_lines(Domain_file)
    tokens = line.split()
    if tokens[0] != '(:predicates':
        print('Bad format Predicates\n')
        return
    start = 1
    while parse_pred_tokens(tokens, start, Domain):
        tokens = skip_empty_lines(Domain_file).split()
        start = 0
        

def parse_method_task_tokens(tokens, start, Domain, method, param_dict):
    task_name = tokens[start].strip('(').strip(')')
    method.taskname = task_name
    Domain.tasks[task_name].methods.append(method)
    i = start
    while i < len(tokens):
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            method.taskparams.append(param_dict[tokens[j][1:].strip(')')])
            j += 1
        i = j


def parse_task_tokens(tokens, start, Domain):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False    
    i = start
    while i < len(tokens):
        task_name = tokens[i].strip('(').strip(')')
        Domain.tasks[task_name] = Task(task_name, True, [])
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            j += 1
        i = j
    return (not tokens[-1][-2:] == '))')    
        

def parse_tasks(Domain_file, Domain):
    line = skip_empty_lines(Domain_file)
    tokens = line.split()
    if tokens[0] != '(:tasks':
        print('Bad format Tasks\n')
        return
    start = 1
    while parse_task_tokens(tokens, start, Domain):
        tokens = skip_empty_lines(Domain_file).split()
        start = 0


def parse_param_tokens(tokens, start, params):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False    
    i = start
    while i < len(tokens):
        param_name = tokens[i].strip('(').strip(')')
        params[param_name[1:]] = len(params)
        i += 1
    return (not tokens[-1][-1] == ')')    


def parse_precond_tokens(tokens, start, params, preconds, Domain):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False  
    i = start
    flag = True
    while i < len(tokens):
        args = []
        pred_name = tokens[i].strip('(').strip(')')
        flag = True
        if pred_name == 'not':
            flag = False
            i += 1
            pred_name = tokens[i].strip('(').strip(')')
        pred = Domain.preds[pred_name]
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            pred_param = tokens[j][1:].strip(')')
            pnum = params[pred_param]
            args.append(pnum)
            j += 1
        i = j
        preconds.append([pred, flag, args])
    if flag:
        return (not tokens[-1][-2:] == '))')
    else:
        return (not tokens[-1][-3:] == ')))')
    
    
def parse_effect_tokens(tokens, start, params, effects, Domain):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False  
    i = start
    flag = True
    while i < len(tokens):
        pred_name = tokens[i].strip('(').strip(')')
        flag = True
        args = []
        if pred_name == 'not':
            flag = False
            i += 1
            pred_name = tokens[i].strip('(').strip(')')
        pred = Domain.preds[pred_name]
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            pred_param = tokens[j][1:].strip(')')
            pnum = params[pred_param]
            args.append(pnum)
            j += 1
        i = j
        effects.append([pred, flag, args])
    if flag:
        return (not tokens[-1][-2:] == '))')
    else:
        return (not tokens[-1][-2:] == ')))') 
    
            
def parse_operator(Domain_file, Domain, init_tokens):
    tokens = init_tokens
    if tokens[0] != '(:operator':
        print('Bad format Operator\n')
        return
    op = Operator(tokens[1], '', [], [], [])
    op_params = dict()
    tokens = skip_empty_lines(Domain_file).split()
    cont = False
    if tokens[0] == ':parameters':
        cont = True
        start = 1
        while parse_param_tokens(tokens, start, op_params):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
    if cont:
        tokens = skip_empty_lines(Domain_file).split()
    if tokens[0] != ':task':
        print('Bad format\n')
        return
    parse_method_task_tokens(tokens, 1, Domain, op, op_params)
    tokens = skip_empty_lines(Domain_file).split()
    cont = False
    if tokens[0] == ':precondition':
        cont = True
        start = 1
        if len(tokens) > 1 and tokens[1] == '(and':
            start = 2
        while parse_precond_tokens(tokens, start, op_params, op.preconds, Domain):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
            if tokens[0] == '(and':
                start = 1
    if cont:
        tokens = skip_empty_lines(Domain_file).split()
    if tokens[0] == ':effect':
        start = 1
        if len(tokens) > 1 and tokens[1] == '(and':
            start = 2
        while parse_effect_tokens(tokens, start, op_params, op.effects, Domain):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
            if tokens[0] == '(and':
                start = 1
    return


def parse_subtask_tokens(tokens, start, param_dict, subtasks, Domain):
    if start >= len(tokens):
        return True
    if tokens[start] == ')':
        return False     
    i = start
    while i < len(tokens):
        subtask_name = tokens[i].strip('(').strip(')')
        subtask_params = []        
        j = i + 1
        while j < len(tokens) and tokens[j][0] == '?':
            subtask_params.append(param_dict[tokens[j][1:].strip(')')])
            j += 1
        i = j
        subtasks.append([Domain.tasks[subtask_name], subtask_params])
    

def parse_method(Domain_file, Domain, init_tokens):
    tokens = init_tokens
    if tokens[0] != '(:method':
        print('Bad format Method\n')
        return
    md = Method(tokens[1], '', [], [], [])
    md_params = dict()
    tokens = skip_empty_lines(Domain_file).split()
    cont = False
    if tokens[0] == ':parameters':
        cont = True
        start = 1
        while parse_param_tokens(tokens, start, md_params):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
    if cont:
        tokens = skip_empty_lines(Domain_file).split()
    if tokens[0] != ':task':
        print('Bad format\n')
        return
    parse_method_task_tokens(tokens, 1, Domain, md, md_params)
    Domain.tasks[tokens[1].strip('(').strip(')')].primitive = False
    tokens = skip_empty_lines(Domain_file).split()
    cont = False
    if tokens[0] == ':precondition':
        cont = True
        start = 1
        if len(tokens) > 1 and tokens[1] == '(and':
            start = 2
        while parse_precond_tokens(tokens, start, md_params, md.preconds, Domain):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
            if tokens[0] == '(and':
                start = 1
    if cont:
        tokens = skip_empty_lines(Domain_file).split()
    if tokens[0] == ':subtasks':
        start = 1
        while parse_subtask_tokens(tokens, start, md_params, md.subtasks, Domain):
            tokens = skip_empty_lines(Domain_file).split()
            start = 0
    return
        

def parse_Domain(Domain_file):
    D = Domain()
    headline = skip_empty_lines(Domain_file)
    D.name = headline[2][:-1]
    parse_predicates(Domain_file, D)
    parse_tasks(Domain_file, D)
    for line in Domain_file:
        tokens = line.strip().split()
        if len(tokens) == 0:
            continue
        elif tokens[0] == '(:operator':
            parse_operator(Domain_file, D, tokens)
        elif tokens[0] == '(:method':
            parse_method(Domain_file, D, tokens) 
    return D