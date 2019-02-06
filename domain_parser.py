from pddl_classes import *

def parse_Domain(Domain_file):
    try:
        for line in Domain_file:
            head = line.split()
            if len(head) != 0:
                break
        for i in range(len(head)):
            head[i] = head[i].strip('(').strip(')')
        D = Domain(head[2])
            
        ### parsing Predicates
    
        for line in Domain_file:
            cur = line.split()
            for i in range(len(cur)):
                cur[i] = cur[i].strip('(').strip(')')            
            if len(cur) != 0:
                break
        for line in Domain_file:
            cur = line.split()
            if len(cur) == 0:
                continue
            elif cur[0] == ')':
                break
            for i in range(len(cur)):
                cur[i] = cur[i].strip('(').strip(')')
            pred_name = cur[0]
            D.preds[pred_name] = Predicate(pred_name, len(cur) - 1)
        
        ### parsing Actions
        
        for line in Domain_file:
            cur = line.split()
            for i in range(len(cur)):
                cur[i] = cur[i].strip('(').strip(')')
            if len(cur) <= 1:
                continue
            act = Action(cur[1], [], [])
            param_map = dict()
            param_num = 0                
            state = 1
            for line in Domain_file:
                cur = line.split()
                for i in range(len(cur)):
                    cur[i] = cur[i].strip('(')
                    if state != 4:
                        cur[i] = cur[i].strip(')')           
                if state == 1:
                    if len(cur) == 0:
                        continue
                    if cur[0] == ':parameters':
                        state = 2
                    continue
                elif state == 2:
                    if len(cur) == 0:
                        continue
                    if cur[0] == ':precondition':
                        state = 3
                        continue
                    else:
                        cur_param_name = cur[0]
                        param_map[cur_param_name] = param_num
                        param_num += 1   
                elif state == 3:                   
                    if len(cur) == 0 or cur[0] == 'and':
                        continue
                    elif cur[0] == ':effect':
                        state = 4
                        continue
                    else:
                        start = (cur[0] == 'not')
                        pred = D.preds[cur[start]]
                        pred_params = [param_map[param] for param in cur[start + 1:]]
                        act.preconds.append([start ^ 1, pred, pred_params])
                elif state == 4:
                    if len(cur) == 0 or cur[0] == 'and':
                        continue                
                    elif cur[0] == ')':
                        break
                    for i in range(len(cur)):
                        cur[i] = cur[i].strip(')') 
                    start = (cur[0] == 'not')
                    pred = D.preds[cur[start]]
                    pred_params = []
                    for param in cur[start + 1:]:
                        pred_params.append(param_map[param])
                    act.effects.append([start ^ 1, pred, pred_params])
            D.acts.append(act)
        return D
    except:
        print('Wrong format: unable to recognize\n')
        return

### example:
Domain_file = open('Domain_example-1.pddl', 'r')
D = parse_Domain(Domain_file)