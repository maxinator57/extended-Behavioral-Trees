from htn_classes import *

world_state = State()

def find_solution(tasks, call_stack, init_state):
    world_state = init_state
    for task_node in tasks:
        call_stack.append([task_node, 0])
        success = True
        if not go(call_stack):
            success = False
            while (not success) and go(call_stack):
                call_stack.append([task_node, 0])
                success = go(call_stack)
        if not success:
            return False  
    return True
        
        
def go(call_stack):
    global world_state
    if len(call_stack) == 0:
        return False
    tnode = call_stack[-1][0]
    m_num = call_stack[-1][1]
    pos = len(call_stack) - 1
    first_call = True
    if len(call_stack[-1]) == 2:
        call_stack[-1].append(world_state.copy())
    else:
        first_call = False
        world_state = call_stack[-1][2].copy()
    print(tnode.task.name, 'task call', str(first_call))
    m_num = call_stack[-1][1]
    ret = False
    for i in range(m_num, len(tnode.methods)):
        world_state = call_stack[-1][2].copy()
        mnode = tnode.methods[i]
        preconds_ok = True
        for precond in mnode.method.preconds:
            args = [mnode.args[i] for i in precond[2]]
            pred = world_state.preds[precond[0].name]
            preconds_ok = preconds_ok and pred.check(precond[1], args)
        ret2 = False
        if preconds_ok:
            ret2 = True
            if type(mnode) == method_node:
                for subtask_node in mnode.subtasks:
                    call_stack.append([subtask_node, 0])
                    ret2 = ret2 and go(call_stack)
                    if not ret2:
                        break
            else:               
                mnode.apply_changes(world_state)                
            if ret2:
                call_stack[pos][1] = i + 1
                ret = True
                break
            else:
                call_stack = call_stack[:pos + 1]
        else:
            continue
    if ret:
        return True
    else:
        call_stack.pop()
        if not first_call:
            return go(call_stack)
        return False